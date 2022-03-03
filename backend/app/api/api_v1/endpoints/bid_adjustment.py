from fastapi import APIRouter, File
from fastapi.params import Form

router = APIRouter(
    tags=["Bid Adjustment"],
    prefix="/bidadjustment"
)



@router.post("/")
async def adjustbid(file: bytes = File(...), data: str = Form(...)):
    pass
