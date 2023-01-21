from fastapi import FastAPI

tank_you = FastAPI()


@tank_you.get("/")
async def root():
    return {"message": "Hello You"}