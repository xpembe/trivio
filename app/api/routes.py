from fastapi import APIRouter, status, HTTPException
from pydantic import ValidationError

# Importing necessary functions and classes from other modules
from .database import readata, writedata, DatabaseError
from .schemas import QuizModel, UpdateQuizModel

# Creating an instance of APIRouter to define route handlers
router = APIRouter()

# Reading initial data from the database
data = readata()


# Route to get all quizzes
@router.get("/", response_model=list[QuizModel])
async def get_quizzes() -> list:
    """
    Get all quizzes.

    Returns:
        list: A list of all quizzes. If no quizzes exist, returns an empty list.
    """
    return data if data else []


# Route to create a new quiz
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_quiz(quiz: QuizModel) -> dict:
    """
    Create a new quiz.

    Args:
        quiz (QuizModel): The quiz data to be created.

    Returns:
        dict: A success message if the quiz is created successfully.

    Raises:
        HTTPException: If the data is invalid (422) or if there is a database error (500).
    """
    try:
        # Append the new quiz to the data list
        data.append(quiz.model_dump())
        # Write the updated data list to the database
        writedata(data)
        # Return a success message
        return {"message": "Quiz created successfully!"}
    except ValidationError:
        # Raise an HTTP 422 error if the data is invalid
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid data!"
        )
    except DatabaseError as err:
        # Raise an HTTP 500 error if there is a database error
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err)
        )


# Route to get a quiz by its ID
@router.get("/{id}")
async def get_quiz(id: int) -> dict:
    """
    Get a quiz by its ID.

    Args:
        id (int): The ID of the quiz to retrieve.

    Returns:
        dict: The quiz data if found.

    Raises:
        HTTPException: If the quiz is not found (404).
    """
    # Find the quiz with the given ID
    quiz = next((quiz for quiz in data if quiz["id"] == id), None)
    if quiz is None:
        # Raise an HTTP 404 error if the quiz is not found
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not found"
        )
    # Return the found quiz
    return quiz


# Route to update a quiz by its ID
@router.patch("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_quiz(id: int, update_quiz: UpdateQuizModel) -> dict:
    """
    Update a quiz by its ID.

    Args:
        id (int): The ID of the quiz to update.
        update_quiz (UpdateQuizModel): The updated quiz data.

    Returns:
        dict: A success message if the quiz is updated successfully.

    Raises:
        HTTPException: If the quiz is not found (404).
    """
    # Find the quiz with the given ID
    quiz = next((quiz for quiz in data if quiz["id"] == id), None)
    if quiz is None:
        # Raise an HTTP 404 error if the quiz is not found
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not found"
        )
    # Update the quiz with the new data, excluding unset fields
    quiz.update(update_quiz.model_dump(exclude_unset=True))
    # Write the updated data list to the database
    writedata(data)
    # Return a success message
    return {"message": "Quiz updated successfully!"}


# Route to delete a quiz by its ID
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_quiz(id: int) -> None:
    """
    Delete a quiz by its ID.

    Args:
        id (int): The ID of the quiz to delete.

    Raises:
        HTTPException: If the quiz is not found (404).
    """
    # Find the quiz with the given ID
    quiz = next((quiz for quiz in data if quiz["id"] == id), None)
    if quiz is None:
        # Raise an HTTP 404 error if the quiz is not found
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not found"
        )
    # Remove the quiz from the data list
    data.remove(quiz)
    # Write the updated data list to the database
    writedata(data)
    # No return statement needed for HTTP 204 No Content
