from fastapi import APIRouter, Depends
from app.database import db

router = APIRouter()

@router.get("/")
async def get_users():
    users = await db.fetch("SELECT * FROM users;")
    return users

@router.post("/users/")
async def create_user(username: str, email: str):
    await db.execute(
        "INSERT INTO users (username, email) VALUES ($1, $2)",
        username,
        email
    )
    return {"message": "User created!"}
