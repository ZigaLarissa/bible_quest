from pydantic import BaseModel, EmailStr

# User Schemas
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: str

    class Config:
        from_orm = True

class User(UserInDB):
    pass

class UserList(BaseModel):
    users: list[User]
    total: int

    class Config:
        from_orm = True

class UserDelete(BaseModel):
    id: str

    class Config:
        from_orm = True


class UserUpdate(BaseModel):
    username: str
    email: EmailStr
    password: str

    class Config:
        from_orm = True