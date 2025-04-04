from fastapi import FastAPI
from config import Config
from database import engine, Base

app = FastAPI()

@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)
