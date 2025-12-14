from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.models.sweet import Sweet
from app.models.user import User
from app.schemas.sweet import SweetCreate, SweetUpdate, SweetResponse
from app.middleware.auth import get_current_user, get_current_admin_user

router = APIRouter(prefix="/api/sweets", tags=["sweets"])


@router.post("", response_model=SweetResponse, status_code=status.HTTP_201_CREATED)
async def create_sweet(
    sweet_data: SweetCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    """Create a new sweet (Admin only)"""
    new_sweet = Sweet(**sweet_data.model_dump())
    db.add(new_sweet)
    db.commit()
    db.refresh(new_sweet)
    return new_sweet


@router.get("", response_model=List[SweetResponse])
async def get_all_sweets(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get all available sweets"""
    sweets = db.query(Sweet).all()
    print(f"[DEBUG] get_all_sweets: Found {len(sweets)} sweets")
    if len(sweets) > 0:
        print(f"[DEBUG] First sweet: ID={sweets[0].id}, Name={sweets[0].name}, Price={sweets[0].price}")
    else:
        print("[DEBUG] No sweets found in database!")
    return sweets


@router.get("/search", response_model=List[SweetResponse])
async def search_sweets(
    name: Optional[str] = Query(None, description="Search by name"),
    category: Optional[str] = Query(None, description="Filter by category"),
    min_price: Optional[float] = Query(None, ge=0, description="Minimum price"),
    max_price: Optional[float] = Query(None, ge=0, description="Maximum price"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Search sweets by name, category, or price range"""
    query = db.query(Sweet)
    
    if name:
        query = query.filter(Sweet.name.ilike(f"%{name}%"))
    
    if category:
        query = query.filter(Sweet.category.ilike(f"%{category}%"))
    
    if min_price is not None:
        query = query.filter(Sweet.price >= min_price)
    
    if max_price is not None:
        query = query.filter(Sweet.price <= max_price)
    
    sweets = query.all()
    return sweets


@router.get("/{sweet_id}", response_model=SweetResponse)
async def get_sweet(
    sweet_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get a specific sweet by ID"""
    sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()
    if not sweet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sweet not found"
        )
    return sweet


@router.put("/{sweet_id}", response_model=SweetResponse)
async def update_sweet(
    sweet_id: int,
    sweet_data: SweetUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update a sweet's details"""
    sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()
    if not sweet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sweet not found"
        )
    
    # Update only provided fields
    update_data = sweet_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(sweet, field, value)
    
    db.commit()
    db.refresh(sweet)
    return sweet


@router.delete("/{sweet_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_sweet(
    sweet_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin_user)
):
    """Delete a sweet (Admin only)"""
    sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()
    if not sweet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sweet not found"
        )
    
    db.delete(sweet)
    db.commit()
    return None

