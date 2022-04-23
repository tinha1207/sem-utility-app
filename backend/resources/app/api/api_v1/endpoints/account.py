from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from ... import deps
from ....schemas.account import Account
from ....services.account import get_all

router = APIRouter(tags=["Account"], prefix="/account")


@router.get("/", response_model=List[Account])
def get_accounts(db: Session = Depends(deps.get_db)):
    return get_all(db)
