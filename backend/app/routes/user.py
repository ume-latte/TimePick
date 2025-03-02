# backend/app/routes/user.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# 定義 Pydantic 模型，用來處理請求體
class User(BaseModel):
    username: str
    password: str

# 用戶註冊
@router.post("/register")
async def register_user(user: User):
    # 實作註冊邏輯
    return {"message": f"User {user.username} registered successfully!"}

# 用戶登入
@router.post("/login")
async def login_user(user: User):
    # 實作登入邏輯
    return {"message": f"User {user.username} logged in successfully!"}
