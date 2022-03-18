from typing import List
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ...models.bid.bid_profile import BidProfile as BidProfileModel
from ...schemas.bid.bid_profile import BidProfileCreate, BidProfile, BidProfileUpdate


def create(bid: BidProfileCreate, db: Session) -> BidProfile:
    new_bid = BidProfileModel(**bid.dict())
    db.add(new_bid)
    db.commit()
    db.refresh(new_bid)
    return new_bid


def read(id: int, db: Session):
    return (
        db.query(BidProfileModel).filter(BidProfileModel.bid_profile_id == id).first()
    )


def read_all(db: Session) -> List[BidProfile]:
    return db.query(BidProfileModel).all()


def update(id: int, updated_bid: BidProfileUpdate, db: Session):
    bid_query = db.query(BidProfileModel).filter(BidProfileModel.bid_profile_id == id)
    if not bid_query.first():
        raise Exception
    bid_query.update(updated_bid.dict(), synchronize_session=False)
    db.commit()
    return bid_query.first()


def delete(id: int, db: Session):
    bid_query = read(id=id, db=db)
    db.delete(bid_query)
    db.commit()
    return bid_query
