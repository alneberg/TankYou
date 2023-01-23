from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

tank_you = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@tank_you.get("/")
async def root():
    return {"message": "Hello You"}