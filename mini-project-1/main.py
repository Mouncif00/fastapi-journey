from fastapi import FastAPI, HTTPException
from typing import List
import asyncio

from models import Member

app = FastAPI()

# In-memory storage (temporary database)
members: List[Member] = []


# GET all members
@app.get("/members/")
async def get_members():
    # simulate async operation
    await asyncio.sleep(1)
    return members


# GET member by ID
@app.get("/members/{member_id}")
async def get_member(member_id: int):

    for member in members:
        if member.id == member_id:
            return member

    raise HTTPException(
        status_code=404,
        detail="Member not found"
    )


# POST create new member
@app.post("/members/")
async def create_member(member: Member):

    # check if ID already exists
    for existing_member in members:
        if existing_member.id == member.id:
            raise HTTPException(
                status_code=400,
                detail="Member with this ID already exists"
            )

    members.append(member)
    return member


# PUT update member
@app.put("/members/{member_id}")
async def update_member(member_id: int, updated_member: Member):

    for index, member in enumerate(members):

        if member.id == member_id:
            members[index] = updated_member
            return updated_member

    raise HTTPException(
        status_code=404,
        detail="Member not found"
    )


# DELETE member
@app.delete("/members/{member_id}")
async def delete_member(member_id: int):

    for index, member in enumerate(members):

        if member.id == member_id:
            deleted_member = members.pop(index)
            return deleted_member

    raise HTTPException(
        status_code=404,
        detail="Member not found"
    )