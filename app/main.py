from fastapi import FastAPI
from .database import db
from .models import create_tables
from .routes import users, posts

app = FastAPI()

@app.on_event("startup")
async def startup():
    await db.connect()
    await create_tables()

@app.on_event("shutdown")
async def shutdown():
    await db.close()

# Routerlarni qo‘shish
app.include_router(users.router, prefix="/users")
# app.include_router(posts.router, prefix="/posts")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
