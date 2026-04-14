from fastapi import APIRouter, HTTPException, status
from app.models.users import User, UserSignIn
from app.database.connection import Database

user_router = APIRouter()
user_db = Database(User)


@user_router.post("/signup")
async def signup(user: User):
    existing = await User.find_one(User.email == user.email)
    if existing:
        raise HTTPException(status_code=409, detail="User exists")

    await user_db.save(user)
    return {"message": "User created"}


@user_router.post("/signin")
async def signin(user: UserSignIn):
    existing = await User.find_one(User.email == user.email)

    if not existing:
        raise HTTPException(status_code=404)

    if existing.password != user.password:
        raise HTTPException(status_code=401)

    return {"message": "Signed in"}