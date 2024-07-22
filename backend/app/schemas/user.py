from pydantic import BaseModel, EmailStr

# User Schemas
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: int

    class Config:
        orm_mode = True

class User(UserInDB):
    pass

class UserList(BaseModel):
    users: list[User]
    total: int

    class Config:
        orm_mode = True