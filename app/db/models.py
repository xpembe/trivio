from sqlmodel import SQLModel, Field
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import JSON
import uuid


class Quiz(SQLModel, table=True):
    """
    Model for a quiz.

    Attributes:
        id (UUID): Unique identifier for the quiz.
        question (str): The quiz question.
        answer (str): The correct answer.
        options (list[str]): A list of possible answers.
    """

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    question: str = Field(max_length=255)
    answer: str = Field(max_length=255)
    options: list[str] = Field(sa_column=Column(JSON))
