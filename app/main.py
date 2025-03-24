from fastapi import FastAPI

from app import models
from app.database import engine
from app.routes import book

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

@app.get('/')
async def root():
    return {"message": "successfully start"}

app.include_router(book.router, prefix="/books")