============================================================
Practice 4 — Path & Query Parameters
============================================================
from fastapi import FastAPI

# Initialize a FastAPI app instance
app = FastAPI()

# Mock database of crew members
# Fixed keys to remove trailing spaces so member["id"] works
crew = [
    { "id": 1,  "name":  "Cosmo ",  "role":  "Captain "},
    { "id": 2,  "name":  "Alice ",  "role":  "Engineer "},
    { "id": 3,  "name":  "Bob ",    "role":  "Scientist "},
]

# TODO: Write an endpoint to get a crew member by PATH parameter
# Endpoint path: /crew_with_path/{crew_id}
@app.get("/crew_with_path/{crew_id}")
def get_crew_path(crew_id: int):
    for member in crew:
        if member["id"] == crew_id:
            return member
    return {"message": "Crew member not found"}

# TODO: Write an endpoint to get a crew member by QUERY parameter
# Endpoint path: /crew_with_query/member
@app.get("/crew_with_query/member")
def get_crew_query(crew_id: int):
    for member in crew:
        if member["id"] == crew_id:
            return member
    return {"message": "Crew member not found"}