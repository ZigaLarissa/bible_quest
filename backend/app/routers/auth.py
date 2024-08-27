from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta, datetime
import hashlib
import jwt

from schemas.auth import Token, TokenData  # Assuming these models are defined as before
from schemas.user import UserCreate, UserInDB   # Import your Pydantic models
from crud import create_user, get_user_by_email  # Import your CRUD functions
from services.database import get_database  # Assuming you have a get_database function
from pymongo.database import Database

# Secret key to encode the JWT token
SECRET_KEY = "mysecretkey"  # Replace with a securely generated secret key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter()

# Dependency to get the database
def get_db() -> Database:
    return get_database()

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Function to authenticate user
def authenticate_user(db: Database, email: str, password: str):
    user = get_user_by_email(db, email)  # Using the CRUD function to get the user by email
    if not user:
        return False
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if user["hashed_password"] != hashed_password:
        return False
    return user

# Function to create JWT access token
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Database = Depends(get_db)  # Inject the database dependency
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["email"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=UserInDB)
async def register_user(
    user: UserCreate,
    db: Database = Depends(get_db)  # Inject the database dependency
):
    created_user = create_user(db, user)  # Using your existing CRUD function
    return created_user
