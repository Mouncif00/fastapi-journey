from fastapi import FastAPI, Request

app = FastAPI()

# Mock database of crew members
crew = [
    {"id": 1, "name": "mahmoud", "role": "Captain"},
    {"id": 2, "name": "Jepstein", "role": "Engineer"},
    {"id": 3, "name": "osama", "role": "Scientist"}
]


# PUT endpoint to update crew member
@app.put("/update_crew/{crew_id}")
async def update_crew(crew_id: int, request: Request):
    data = await request.json()

    name = data.get("name")
    role = data.get("role")

    # Search for crew member
    for member in crew:
        if member["id"] == crew_id:
            if name:
                member["name"] = name
            if role:
                member["role"] = role

            return {
                "message": "Crew member updated successfully",
                "crew_member": member
            }

    return {"message": "Crew member not found"}