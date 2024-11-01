from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.profile_router import profile_router
from routers.user_router import user_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(profile_router)
app.include_router(user_router)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


