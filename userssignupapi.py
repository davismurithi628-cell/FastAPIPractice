from fastapi import APIRouter, Query, Body, Path, Depends
from pydantic import BaseModel
router = APIRouter(prefix="/signup")

class UserInfo(BaseModel):
    first_name: str = Body(..., max_length=100, min_length=2,
                           pattern="^[a-zA-Z]$")

    second_name: str = Body(..., max_length=100, min_length=2,
                           pattern="^[a-zA-Z]$")

    surname: str = Body(..., max_length=100, min_length=2,
                           pattern="^[a-zA-Z]$")

    email: str = Body(..., max_length=100, min_length=2,
                           pattern="^[a-zA-Z@.]$")

    phone_number: str = Body(..., max_length=100, min_length=2,
                           pattern="^[0-9+]$")


@router.post("/info")
def get_user_info_as_dict(u_info: UserInfo):
    return u_info


