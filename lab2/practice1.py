from fastapi import FastAPI, Request

app = FastAPI()

# Mock database of crew members
crew = [


    {"id": 1, "name": "Cosmo", "role": "Captain"},
    {"id": 2, "name": "Alice", "role": "Engineer"},
    {"id": 3, "name": "Bob", "role": "Scientist"}
]


# POST endpoint to add a new crew member
@app.post("/add_crew/")



async def add_crew(request: Request):
    data = await request.json()
    
    name = data.get("name")


    role = data.get("role")

    # Basic validation
    if not name or not role:
        return {"error": "Both name and role are required"}

    # Generate new ID
    if crew:
        new_id = max(member["id"] for member in crew) + 1
    else:
        new_id = 1

    new_member = {
          "id": new_id,
        "name": name,
    "role": role
    }

    crew.append(new_member)

    return {
        "message": "Crew member added successfully",
        "crew_member": new_member
    }