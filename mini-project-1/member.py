from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import asyncio

from models import Member
from database import managed_db   # ✅ NEW

member_router = APIRouter()

templates = Jinja2Templates(directory="mini-project-1/templates")

# ❌ REMOVE THIS:
# members: List[Member] = []


# ---------------- API ENDPOINTS ----------------

@member_router.get("/members/")
async def get_members():
    await asyncio.sleep(1)
    with managed_db() as db:
        return db.get_all()
    

@member_router.get("/members/{member_id}")
async def get_member(member_id: int):
    with managed_db() as db:
        member = db.get(member_id)

        if member is None:
            raise HTTPException(
                status_code=404,
                detail=f"Member with ID {member_id} was not found"
            )

        return member


@member_router.post("/members/")
async def create_member(member: Member):
    with managed_db() as db:
        new_id = db.create(member)
        return {"id": new_id}


@member_router.put("/members/{member_id}")
async def update_member(member_id: int, updated_member: Member):
    with managed_db() as db:
        updated = db.update(member_id, updated_member)

        if updated is None:
            raise HTTPException(
                status_code=404,
                detail=f"Member with ID {member_id} not found"
            )

        return updated


@member_router.delete("/members/{member_id}")
async def delete_member(member_id: int):
    with managed_db() as db:
        member = db.get(member_id)

        if member is None:
            raise HTTPException(
                status_code=404,
                detail=f"Member with ID {member_id} not found"
            )

        db.delete(member_id)
        return {"message": "Deleted"}


# ---------------- HTML ROUTES ----------------

@member_router.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    with managed_db() as db:
        members = db.get_all()

    return templates.TemplateResponse("home.html", {
        "request": request,
        "members": members
    })


@member_router.get("/member/{id}", response_class=HTMLResponse)
async def get_member_page(request: Request, id: int):
    with managed_db() as db:
        member = db.get(id)

        if member is None:
            raise HTTPException(status_code=404, detail="Member not found")

    return templates.TemplateResponse("member.html", {
        "request": request,
        "member": member
    })