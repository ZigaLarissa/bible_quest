from pydantic import BaseModel
from schemas.category import Category

# Question Schemas
class QuestionBase(BaseModel):
    question_text: str
    correct_answer: str
    incorrect_answer1: str
    incorrect_answer2: str
    incorrect_answer3: str

class QuestionCreate(QuestionBase):
    category_id: int

class Question(QuestionBase):
    id: int
    category_id: int
    category: Category

    class Config:
        orm_mode = True
