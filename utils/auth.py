# utils/auth.py
from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from settings.config import supabase

security = HTTPBearer()

async def verify_token(
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    token = credentials.credentials
    try:
        # Verify the token using the Supabase client
        auth_response = supabase.auth.get_user(jwt=token)
        if not auth_response.user:
            raise HTTPException(status_code=401, detail="Invalid or expired token")
        return auth_response.user
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Token verification failed: {str(e)}")
