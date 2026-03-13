from pydantic import BaseModel, Field
from typing import List, Optional

class WorkoutSession(BaseModel):
    id: int
    exercise: str = Field(min_length=3, max_length=50)
    duration_minutes: int = Field(gt=0, le=180)
    calories_burned: int = Field(ge=0)

class Member(BaseModel):
    id: int
    name: str = Field(min_length=3, max_length=50)
    age: int = Field(gt=15, lt=100)
    membership_type: str = Field(default="standard")
    sessions: List[WorkoutSession] = []