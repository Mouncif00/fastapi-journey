from fastapi import FastAPI, Request

app = FastAPI()

crew = [
    {"id": 1, "name": "saddam", "role": "Captain"},
    {"id": 2, "name": "gadafi", "role": "Engineer"},
    {"id": 3, "name": "osama", "role": "Scientist"}
]


@app.get("/members/{crew_id}")
async def read_crew_member(crew_id: int):
    for c in crew:
        if c["id"] == crew_id:
            return c
    return {"message": "Crew member not found"}


@app.post("/members/")
async def add_crew_member(request: Request):
    data = await request.json()
    name = data["name"]
    role = data["role"]

    new_id = len(crew) + 1

    new_member = {
        "id": new_id,
        "name": name,
        "role": role
    }

    crew.append(new_member)
    return new_member


@app.put("/members/{crew_id}")
async def update_crew_member(crew_id: int, request: Request):
    data = await request.json()

    for c in crew:
        if c["id"] == crew_id:
            c["name"] = data["name"]
            c["role"] = data["role"]
            return c

    return {"message": "Crew member not found"}


@app.delete("/members/{crew_id}")
async def delete_crew_member(crew_id: int):
    for c in crew:
        if c["id"] == crew_id:
            crew.remove(c)
            return {"message": "Deleted"}

    return {"message": "Crew member not found"}