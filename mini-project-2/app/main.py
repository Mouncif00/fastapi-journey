from fastapi import FastAPI
from database.connection import Settings
from app.routes.events import event_router
from app.routes.users import user_router

app = FastAPI()

app.include_router(event_router, prefix="/event")
app.include_router(user_router, prefix="/user")


@app.on_event("startup")
async def start_db():
    settings = Settings()
    await settings.initialize_database()