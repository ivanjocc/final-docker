from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class CVBase(BaseModel):
    candidate_name: str
    skills: str

class CVCreate(CVBase):
    user_id: int

class JobOfferBase(BaseModel):
    title: str
    required_skills: str

class JobOfferCreate(JobOfferBase):
    recruiter_id: int
