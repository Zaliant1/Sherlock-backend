
from fastapi import FastAPI
import foobar
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["localhost:3000" "127.0.0.1:3000"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"hello": "world"}


@app.get("/user_search/{user_input}/")
def searching_for_user(user: str):
    return foobar.user_search(user)
