import sys
sys.path.append('sherlock/sherlock')
import sherlock
from fastapi import FastAPI
from pydantic import BaseModel

class SherlockQuery(BaseModel):
    username: str

app = FastAPI()

@app.post("/")
async def endpoint(item: SherlockQuery):
    sherlock_json = sherlock.req_json(item.username)
    return sherlock_json