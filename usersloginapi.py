from fastapi import APIRouter, Query,Body,Path,Depends

router = APIRouter(prefix="/login")
@router.post("/details")
def verify_details():
    return


