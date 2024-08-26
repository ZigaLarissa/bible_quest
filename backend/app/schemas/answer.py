from pydantic import BaseModel, List

# Answer Schemas
class QuestionResponse(BaseModel):
    id: int
    question_text: str
    answers: List[str]

    class Config:
        from_orm = True

class SubmitAnswer(BaseModel):
    question_id: int
    selected_answer: str

class ProgressSummary(BaseModel):
    total_questions: int
    correct_answers: int
    accuracy: float

    class Config:
        from_orm = True