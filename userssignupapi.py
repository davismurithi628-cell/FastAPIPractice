from fastapi import APIRouter, Query, Body, Path, Depends
from pydantic import BaseModel
router = APIRouter(prefix="/signup")





@router.post("/info")
def get_user_info_as_dict(first_name: str = Body(..., max_length=100, min_length=2),

    second_name: str = Body(..., max_length=100, min_length=2),

    surname: str = Body(..., max_length=100, min_length=2),

    email: str = Body(..., max_length=100, min_length=2),

    phone_number: str = Body(..., max_length=100, min_length=2)):
    return {"first_name": first_name,
            "second_name": second_name,
            "surname": surname,
            "email": email,
            "phone_number": phone_number}
