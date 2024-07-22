from fastapi import APIRouter, Depends, HTTPException
from pymongo.database import Database
from bson import ObjectId

from app.schemas.user import User, UserCreate, UserList
from app.crud import get_users, get_user_by_email, get_user, create_user, delete_user
from app.services.database import get_database

router = APIRouter()

# Dependency
def get_db() -> Database:
    return get_database()

@router.post("/users/", response_model=User, tags=["users"])
async def create_new_user(user: UserCreate, db: Database = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)

@router.get("/users/", response_model=UserList, tags=["users"])
async def read_users(skip: int = 0, limit: int = 10, db: Database = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return {"users": users}

@router.get("/user/{user_id}", response_model=User, tags=["users"])
async def read_user(user_id: str, db: Database = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/user/{user_id}", response_model=User, tags=["users"])
async def remove_user(user_id: str, db: Database = Depends(get_db)):
    db_user = delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user