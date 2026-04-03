from fastapi import FastAPI
from apirouters import usersloginapi,userssignupapi
app = FastAPI()
@app.get("/")
def greet():
    return "Hi Dave"
app.include_router(userssignupapi.router)
