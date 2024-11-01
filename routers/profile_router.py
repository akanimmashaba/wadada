from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from models.profile import Profile
from settings.database import get_session
from sqlalchemy import select
from utils.auth import verify_token
from schemas.profile_schemas import CreateProfile

profile_router = APIRouter(
    prefix="/profile",
    tags=["profile"]
)

@profile_router.post("/profile")
async def create_profile(
    profile: CreateProfile,
    session: AsyncSession = Depends(get_session), 
    user=Depends(verify_token)):

    try:
        supabase_uid = user.id

        existing_profile = await session.execute(
            select(Profile).where(Profile.supabase_uid == supabase_uid)
        )
        if existing_profile.scalar_one_or_none():
            raise HTTPException(status_code=409, detail="Profile already exists")
            
        
        new_profile = Profile(
            supabase_uid=supabase_uid,
            name=profile.name,
            dob=profile.dob,
            bio=profile.bio
        )
        session.add(new_profile)
        await session.commit()
        await session.refresh(new_profile)
        return {"message": "Profile created successfully", "profile": new_profile}
    
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

