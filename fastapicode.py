from fastapi import FastAPI
from apirouters import usersloginapi,userssignupapi
app = FastAPI()
app.include_router(userssignupapi.router)
