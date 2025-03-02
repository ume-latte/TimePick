# backend/app/main.py

from fastapi import FastAPI
from app.routes import user_router, item_router, order_router

app = FastAPI()

# 註冊路由
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(item_router, prefix="/items", tags=["items"])
app.include_router(order_router, prefix="/orders", tags=["orders"])

# 根路由
@app.get("/")
def read_root():
    return {"message": "Welcome to TimePick API!"}
