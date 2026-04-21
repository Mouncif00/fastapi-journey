from fastapi import FastAPI, Request

app = FastAPI()


crew = [
    {"id": 1, "name": "saddam", "role": "Captain"},
    {"id": 2, "name": "Jepstein", "role": "Engineer"},
    {"id": 3, "name": "osama", "role": "Scientist"}
]


@app.put("/update_crew/{crew_id}")

async def update_crew(crew_id: int, request: Request):
    data = await request.json()

    
    name = data.get("name")
    role = data.get("role")

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