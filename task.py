from fastapi import  FastAPI
from pydantic import BaseModel 

app = FastAPI()

crew= [

    {"id" :1,"name": "Cosmo", "role":"captain","experience":10},

    {"id" :2,"name": "Alice", "role":"Engineer","experience":8},

    {"id" :3,"name": "Bob","role":"Scientist","experience":5} 
 

]
class Crewmember(BaseModel):
    name :str
   
    experience : int 

@app.get("/crew/{crew_id}",response_model=Crewmember)
async def read_crew_member(crew_id: int):
    for member in crew:
        if member ["id"] == crew_id:
            return member 