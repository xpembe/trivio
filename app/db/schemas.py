from pydantic import BaseModel


class QuizModel(BaseModel):
    """
    Schema for a quiz.

    Attributes:
        id (int): The unique identifier for the quiz.
        question (str): The question text of the quiz.
        answer (str): The correct answer to the quiz question.
        options (list[str]): A list of possible answer options.
    """

    id: int
    question: str
    answer: str
    options: list[str]


class UpdateQuizModel(BaseModel):
    """
    Schema for updating a quiz.

    Attributes:
        question (str): The updated question text of the quiz.
        answer (str): The updated correct answer to the quiz question.
        options (list[str]): The updated list of possible answer options.
    """

    question: str
    answer: str
    options: list[str]
