from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..models.account import Account as AccountModel


def get_all(db: Session):
    accounts = db.query(AccountModel).all()
    return accounts
