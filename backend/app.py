from fastapi import FastAPI
from routes.books import router as BooksRouter

app = FastAPI()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "App is running"}

app.include_router(BooksRouter)
