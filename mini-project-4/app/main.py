from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from typing import List
import uuid
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")
# Store polls in memory
polls = {}

# Store active websocket connections
connections = {}


class ConnectionManager:

    async def connect(self, poll_id: str, websocket: WebSocket):

        await websocket.accept()

        if poll_id not in connections:
            connections[poll_id] = []

        connections[poll_id].append(websocket)

    def disconnect(self, poll_id: str, websocket: WebSocket):

        if poll_id in connections:
            connections[poll_id].remove(websocket)

    async def broadcast(self, poll_id: str, message: dict):

        if poll_id in connections:

            for connection in connections[poll_id]:
                await connection.send_json(message)


manager = ConnectionManager()

# Request body for creating a poll
class PollCreate(BaseModel):
    question: str
    options: List[str]




@app.get("/", response_class=HTMLResponse)
async def frontend(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


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

# VOTE ON POLL
@app.post("/polls/{poll_id}/vote")
def vote_poll(poll_id: str, option: str):

    if poll_id not in polls:
        return {"error": "Poll not found"}

    poll = polls[poll_id]

    if option not in poll["votes"]:
        return {"error": "Invalid option"}

    poll["votes"][option] += 1

    return {
        "message": "Vote added",
        "poll": poll
    }


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


@app.websocket("/ws/polls/{poll_id}")
async def websocket_poll(websocket: WebSocket, poll_id: str):

    await manager.connect(poll_id, websocket)

    try:

        while True:

            data = await websocket.receive_json()

            option = data.get("option")

            if poll_id not in polls:
                await websocket.send_json({
                    "error": "Poll not found"
                })
                continue

            poll = polls[poll_id]

            if option not in poll["votes"]:
                await websocket.send_json({
                    "error": "Invalid option"
                })
                continue

            # Add vote
            poll["votes"][option] += 1

            # Broadcast updated poll to ALL clients
            await manager.broadcast(
                poll_id,
                {
                    "message": "Vote updated",
                    "poll": poll
                }
            )

    except WebSocketDisconnect:

        manager.disconnect(poll_id, websocket)