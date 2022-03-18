from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from typing import Optional, List

from ...deps import get_db
from ....services.bid import bid_profile
from ....schemas.bid.bid_profile import BidProfileCreate, BidProfile, BidProfileUpdate


router = APIRouter(tags=["Bid"], prefix="/bid")


@router.get("/bid_profile", response_model=List[BidProfile])
def get_all_bid_profiles(db: Session = Depends(get_db)):
    return bid_profile.read_all(db=db)


@router.post("/bid_profile", response_model=BidProfile)
def create_bid_profile(bid: BidProfileCreate, db: Session = Depends(get_db)):
    return bid_profile.create(bid=bid, db=db)


@router.get("/bid_profile/{id}", response_model=BidProfile)
def get_bid_profile(id: int, db: Session = Depends(get_db)):
    bid = bid_profile.read(id=id, db=db)
    if not bid:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Bid Profile not found."
        )
    return bid


@router.put("/bid_profile/{id}", response_model=BidProfile)
def update_bid_profile(
    id: int, updated_bid: BidProfileUpdate, db: Session = Depends(get_db)
):
    bid = bid_profile.read(id=id, db=db)
    if not bid:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Bid Profile not found."
        )
    return bid_profile.update(id=id, updated_bid=updated_bid, db=db)


@router.delete("/bid_profile/{id}")
def delete_bid_profile(id: int, db: Session = Depends(get_db)):
    bid = bid_profile.read(id=id, db=db)
    if not bid:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Bid Profile not found."
        )
    return bid_profile.delete(id=id, db=db)
