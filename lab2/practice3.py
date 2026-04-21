from fastapi import FastAPI

app = FastAPI()


crew = [
    {"id": 1, "name": "saddam", "role": "Captain"},
    {"id": 2, "name": "gadafi", "role": "Engineer"},
    {"id": 3, "name": "osama", "role": "Scientist"}
]


@app.delete("/delete_member/{crew_id}")
async def delete_member(crew_id: int):
    
    for member in crew:
        if member["id"] == crew_id:
            crew.remove(member)
            return {
                "message": "Crew member deleted successfully",
                "deleted_member": member
            }

    return {"message": "Crew member not found"}