import sys
sys.path.append('sherlock/sherlock')
import sherlock
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class SherlockQuery(BaseModel):
    username: str

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
    sherlock_json = sherlock.req_json(item.username)
    return sherlock_json