from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel import SQLModel, create_engine
from app.config import Config

import json

# Path to the JSON file that stores quiz data
DATA_PATH: str = "./quizzes.json"


class DatabaseError(Exception):
    """
    Custom exception class for database errors.
    """

    pass


def readata() -> dict:
    """
    Read data from the JSON file.

    Returns:
        dict: The data read from the JSON file.

    Raises:
        DatabaseError: If there is an error reading the file.
    """
    try:
        # Open the JSON file and load its content
        with open(DATA_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, PermissionError, json.JSONDecodeError) as err:
        # Raise a custom DatabaseError if any of the specified exceptions occur
        raise DatabaseError(f"An unexpected error occurred: {str(err)}")


def writedata(data: list) -> None:
    """
    Write data to the JSON file.

    Args:
        data (list): The data to be written to the JSON file.

    Raises:
        DatabaseError: If there is an error writing to the file.
    """
    try:
        # Open the JSON file and write the data to it
        with open(DATA_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except IOError as err:
        # Raise a custom DatabaseError if an IOError occurs
        raise DatabaseError(f"An unexpected error occurred: {str(err)}")


# Connection to the database
engine = AsyncEngine(create_engine(url=Config.DATABASE_URL, echo=True))


async def init_db():
    """
    Initiate and create tables in the database.
    """
    async with engine.begin() as conn:
        from .models import Quiz

        await conn.run_sync(SQLModel.metadata.create_all)
