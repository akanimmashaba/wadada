from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from settings.database import get_session
from utils.auth import verify_token
from settings.config import supabase  # Import your Supabase client
from models.profile_models.image import Image  # Import your Image model
from sqlalchemy import select
from typing import List


image_router = APIRouter(
    prefix="/images",
    tags=["images"]
)

@image_router.post("/upload")
async def upload_image(
    file: UploadFile = File(...),
    session: AsyncSession = Depends(get_session),
    user=Depends(verify_token)
):
    try:
        # Upload the file to Supabase storage
        file_path = f"images/{user.id}/{file.filename}"  # Adjust the path as needed
        response = supabase.storage.from_("your_bucket_name").upload(file_path, file.file)

        if response.get('error'):
            raise HTTPException(status_code=400, detail="Error uploading file to Supabase")

        # Get the public URL for the uploaded file
        public_url = supabase.storage.from_("your_bucket_name").get_public_url(file_path)['publicURL']

        # Save the image information in the database
        existing_images = await session.exec(select(Image).where(Image.profile_id == user.id))
        max_sort_order = max((image.sort_order for image in existing_images), default=-1)
        new_image = Image(
            profile_id=user.id,
            url=public_url,
            sort_order=max_sort_order + 1  # Increment sort_order
        )
        session.add(new_image)
        await session.commit()
        await session.refresh(new_image)

        return {"message": "Image uploaded successfully", "image": new_image}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@image_router.get("/")
async def get_images(user=Depends(verify_token), session: AsyncSession = Depends(get_session)):
    try:
        images = await session.exec(select(Image).where(Image.profile_id == user.id).order_by(Image.sort_order))
        return {"images": images.all()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@image_router.put("/sort")
async def update_sort_order(sort_orders: List[int], user=Depends(verify_token), session: AsyncSession = Depends(get_session)):
    try:
        images = await session.exec(select(Image).where(Image.profile_id == user.id))
        images_dict = {image.id: image for image in images}

        # Update sort_order based on provided list
        for index, image_id in enumerate(sort_orders):
            if image_id in images_dict:
                images_dict[image_id].sort_order = index  # Set sort_order to its new position

        await session.commit()
        return {"message": "Sort order updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
