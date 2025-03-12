from pydantic import BaseModel
from typing import Optional

# ✅ User Signup Schema
class UserSignup(BaseModel):
    username: str
    email: str
    password: str
    name: str

# ✅ User Login Schema
class UserLogin(BaseModel):
    username: str
    password: str

# ✅ Token Response Schema
class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    name: str

# ✅ Resume Create Schema
class ResumeCreate(BaseModel):
    name: str
    email: str
    phone: str
    summary: Optional[str] = None
    skills: str
    experience: str

# ✅ Resume Update Schema (Optional fields for updates)
class ResumeUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    summary: Optional[str] = None
    skills: Optional[str] = None
    experience: Optional[str] = None

# ✅ Resume Response Schema (For API responses)
class ResumeResponse(BaseModel):
    id: int
    user_id: int
    name: str
    email: str
    phone: str
    summary: Optional[str]
    skills: str
    experience: str

    class Config:
        from_attributes = True
