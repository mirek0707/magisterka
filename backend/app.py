from fastapi import FastAPI
from routes.books import router as BooksRouter
from routes.users import router as UsersRouter
from routes.shelves import router as ShelvesRouter

app = FastAPI()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "App is running"}


app.include_router(BooksRouter)
app.include_router(UsersRouter)
app.include_router(ShelvesRouter)
