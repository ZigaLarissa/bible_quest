from pydantic import BaseModel
from datetime import datetime
from schemas.user import User
from schemas.question import Question

# UserProgress Schemas
class UserProgressBase(BaseModel):
    is_correct: bool

class UserProgressCreate(UserProgressBase):
    user_id: int
    question_id: int

class UserProgress(UserProgressBase):
    id: int
    user_id: int
    question_id: int
    timestamp: datetime
    user: User
    question:   Question

    class Config:
        orm_mode = True