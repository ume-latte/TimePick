# backend/app/models/user_model.py

from pydantic import BaseModel
from typing import Optional

# 定義用戶模型
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool = True

    class Config:
        orm_mode = True  # 讓 Pydantic 模型與 ORM 模型兼容
