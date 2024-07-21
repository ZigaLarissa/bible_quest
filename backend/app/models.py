from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from services.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    progress = relationship("UserProgress", back_populates="user")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    questions = relationship("Question", back_populates="category")


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String)
    correct_answer = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))
    incorrect_answer1 = Column(String)
    incorrect_answer2 = Column(String)
    incorrect_answer3 = Column(String)

    category = relationship("Category", back_populates="questions")
    progress = relationship("Progress", back_populates="questions")

class UserProress(Base):
    __tablename__ = "user_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    is_correct = Column(Boolean, default=False)
    time_stamp = Column(DateTime)

    user = relationship("User", back_populates="progress")
    question = relationship("Question", back_populates="progress")
