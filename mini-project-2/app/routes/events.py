from fastapi import APIRouter, HTTPException, status
from typing import List
from beanie import PydanticObjectId
from app.models.events import Event, EventUpdate
from app.database.connection import Database

event_router = APIRouter()
event_db = Database(Event)


@event_router.get("/", response_model=List[Event])
async def get_all_events():
    return await event_db.get_all()


@event_router.get("/{id}", response_model=Event)
async def get_event(id: PydanticObjectId):
    event = await event_db.get(id)
    if not event:
        raise HTTPException(status_code=404)
    return event


@event_router.post("/new")
async def create_event(event: Event):
    await event_db.save(event)
    return {"message": "Event created"}


@event_router.put("/{id}")
async def update_event(id: PydanticObjectId, body: EventUpdate):
    updated = await event_db.update(id, body)
    if not updated:
        raise HTTPException(status_code=404)
    return updated


@event_router.delete("/{id}")
async def delete_event(id: PydanticObjectId):
    deleted = await event_db.delete(id)
    if not deleted:
        raise HTTPException(status_code=404)
    return {"message": "Deleted"}