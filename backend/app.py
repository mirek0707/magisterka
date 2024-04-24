from fastapi import FastAPI
from routes.books import router as BooksRouter
from routes.users import router as UsersRouter
from routes.shelves import router as ShelvesRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "App is running"}


app.include_router(BooksRouter)
app.include_router(UsersRouter)
app.include_router(ShelvesRouter)
