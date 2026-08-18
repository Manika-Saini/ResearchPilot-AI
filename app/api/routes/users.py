from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user, get_user, get_users


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/", response_model=UserResponse)
def create_new_user(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    try:
        return create_user(db, user_data)

    except ValueError as error:
        raise HTTPException(
            status_code=409,
            detail=str(error)
        )


@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = get_user(db, user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.get("/", response_model=list[UserResponse])
def get_all_users(
    db: Session = Depends(get_db)
):
    return get_users(db)