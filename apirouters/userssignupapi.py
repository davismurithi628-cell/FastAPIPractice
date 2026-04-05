from fastapi import APIRouter, Query, Body, Path, Depends
from pydantic import BaseModel
import database
router = APIRouter(prefix="/signup")





@router.post("/info")
def get_user_info_as_dict(first_name: str = Body(..., max_length=100, min_length=2),

    second_name: str = Body(..., max_length=100, min_length=2),

    surname: str = Body(..., max_length=100, min_length=2),

    email: str = Body(..., max_length=100, min_length=2),

    phone_number: str = Body(..., max_length=100, min_length=2)):
    query_object = database.QueryDatabase(database_="Kinjo")
    query_object.insert_data_into_table_query(col_names_list=["first_name","second_name","surname","email","phone_number"],
                                              table_name="signup_info",
                                              data_to_insert_list=[first_name,second_name,surname,email,phone_number])
     
    print("success")