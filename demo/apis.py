from fastapi import FastAPI
import os
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Sample(BaseModel):
    key: str
    uri: str
    data: list


class Visitor(BaseModel):
    email: str
    comments: str


@app.get("/health")
async def root():
    return {"message": "healthy"}


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.post("/test")
async def test(input):
    return input


@app.get("/get")
async def get(input):
    response = supabase.table('demo').select(input).execute()
    return response


@app.post("/create")
async def create(sample: Sample):
    print("recvd post", sample)
    data, count = supabase.table('demo').upsert({
        "key": sample.key,
        "uri": sample.uri,
        "data": sample.data
    }).execute()

    print("storing in db - data, count", data, count)
    return sample


@app.post("/waitlist")
async def waitlist(visitor: Visitor):
    print("User visited:", visitor)
    supabase.table('visitor').insert({
        "email": visitor.email,
        "comments": visitor.comments
    }).execute()
    print(f"visitor: {visitor.email} inserted.")
    return "Thanks for reaching out. We'll get back to you soon."
