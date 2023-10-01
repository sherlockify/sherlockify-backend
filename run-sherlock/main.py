import sys
sys.path.append('sherlock/sherlock')
import sherlock
from res_queue import QueryNotifyQueue
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse
import asyncio
from _thread import start_new_thread
from pydantic import BaseModel
import json

STREAM_DELAY = 0.1
query_notify = QueryNotifyQueue()

class SherlockQuery(BaseModel):
    username: str
    extra: bool

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.post("/")
async def endpoint(item: SherlockQuery):
    query_notify.clearQueue()
    start_new_thread(sherlock.req_json, (item.username, item.extra, query_notify))
    return item

@app.get("/stream")
async def stream(request: Request):
    async def event_generator():
        item = None
        while True:
            if await request.is_disconnected():
                break

            if not query_notify.queueEmpty():
                item = query_notify.queuePop()
                yield json.dumps(item)

            if item and ("stop" in item):
                break

            await asyncio.sleep(STREAM_DELAY)
    
    return EventSourceResponse(event_generator())
