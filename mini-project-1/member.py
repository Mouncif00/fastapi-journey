from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List
import asyncio

from models import Member

member_router = APIRouter()

templates = Jinja2Templates(directory="mini-project-1/templates")

# In-memory database
members: List[Member] = []


# ---------------- API ENDPOINTS ----------------

@member_router.get("/members/")
async def get_members():
    await asyncio.sleep(1)
    return members


@member_router.get("/members/{member_id}")
async def get_member(member_id: int):
    for member in members:
        if member.id == member_id:
            return member

    raise HTTPException(
        status_code=404,
        detail=f"Member with ID {member_id} was not found"
    )


@member_router.post("/members/")
async def create_member(member: Member):
    for m in members:
        if m.id == member.id:
            raise HTTPException(
                status_code=400,
                detail="Member with this ID already exists"
            )

    members.append(member)
    return member


@member_router.put("/members/{member_id}")
async def update_member(member_id: int, updated_member: Member):
    for i, m in enumerate(members):
        if m.id == member_id:
            members[i] = updated_member
            return updated_member

    raise HTTPException(
        status_code=404,
        detail=f"Member with ID {member_id} not found"
    )


@member_router.delete("/members/{member_id}")
async def delete_member(member_id: int):
    for i, m in enumerate(members):
        if m.id == member_id:
            return members.pop(i)

    raise HTTPException(
        status_code=404,
        detail=f"Member with ID {member_id} not found"
    )


# ---------------- HTML ROUTES ----------------

@member_router.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {
        "request": request,
        "members": members
    })


@member_router.get("/member/{id}", response_class=HTMLResponse)
async def get_member_page(request: Request, id: int):
    for member in members:
        if member.id == id:
            return templates.TemplateResponse("member.html", {
                "request": request,
                "member": member
            })

    raise HTTPException(status_code=404, detail="Member not found")