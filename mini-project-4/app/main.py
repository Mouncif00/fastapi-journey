from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uuid

app = FastAPI()

# Store polls in memory
polls = {}

# Request body for creating a poll
class PollCreate(BaseModel):
    question: str
    options: List[str]


@app.get("/")
def home():
    return {"message": "Mini Project 4 Running"}


# CREATE POLL
@app.post("/polls")
def create_poll(poll: PollCreate):

    poll_id = str(uuid.uuid4())

    polls[poll_id] = {
        "id": poll_id,
        "question": poll.question,
        "options": poll.options,
        "votes": {option: 0 for option in poll.options}
    }

    return polls[poll_id]


# GET ALL POLLS
@app.get("/polls")
def get_polls():
    return list(polls.values())


# GET SINGLE POLL
@app.get("/polls/{poll_id}")
def get_poll(poll_id: str):

    if poll_id not in polls:
        return {"error": "Poll not found"}

    return polls[poll_id]


# DELETE POLL
@app.delete("/polls/{poll_id}")
def delete_poll(poll_id: str):

    if poll_id not in polls:
        return {"error": "Poll not found"}

    deleted_poll = polls.pop(poll_id)

    return {
        "message": "Poll deleted",
        "poll": deleted_poll
    }