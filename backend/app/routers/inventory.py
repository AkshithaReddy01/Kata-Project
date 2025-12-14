from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import get_db
from app.models.sweet import Sweet
from app.models.user import User
from app.schemas.sweet import SweetResponse
from app.middleware.auth import get_current_user, get_current_admin_user

router = APIRouter(prefix="/api/sweets", tags=["inventory"])


class RestockRequest(BaseModel):
    quantity: int


@router.post("/{sweet_id}/purchase", response_model=SweetResponse)
async def purchase_sweet(
    sweet_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Purchase a sweet, decreasing its quantity by 1"""
    sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()
    if not sweet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sweet not found"
        )
    
    if sweet.quantity <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Sweet is out of stock"
        )
    
    sweet.quantity -= 1
    db.commit()
    db.refresh(sweet)
    return sweet


@router.post("/{sweet_id}/restock", response_model=SweetResponse)
async def restock_sweet(
    sweet_id: int,
    restock_data: RestockRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    """Restock a sweet, increasing its quantity (Admin only)"""
    if restock_data.quantity <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Restock quantity must be greater than 0"
        )
    
    sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()
    if not sweet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sweet not found"
        )
    
    sweet.quantity += restock_data.quantity
    db.commit()
    db.refresh(sweet)
    return sweet

