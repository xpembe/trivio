import requests
import json


# Base URL for the API endpoints
API_URL = "http://localhost:8000/api/v1/quizzes"


def get_all_quizzes():
    """
    Retrieve and print all quizzes from the API.

    Sends a GET request to the API to retrieve all quizzes.
    Prints each quiz's ID, question, answer, and options.

    Raises:
        HTTPError: If the request fails.

    Prints:
        str: A formatted string with all quizzes or an error message.
    """
    # Send a GET request to the API to retrieve all quizzes
    response = requests.get(API_URL)

    # Check if the request to get all quizzes was successful
    if response.status_code == 200:
        # Parse the JSON response
        quizzes = response.json()
        # Iterate through each quiz and print its details
        for quiz in quizzes:
            print(json.dumps(quiz, indent=4))
    else:
        # Prints an error message if the request failed
        print("Failed to retrieve quizzes")


def create_quiz():
    """
    Create a new quiz using user input.

    Prompts the user to enter quiz details (ID, question, answer, options).
    Sends a POST request to the API to create the quiz.

    Raises:
        HTTPError: If the request fails.

    Prints:
        str: A message indicating whether the quiz was created successfully or not.
    """
    # Collect quiz details from user input
    quiz = {
        "id": int(input("Enter quiz ID: ")),
        "question": input("Enter quiz question: "),
        "answer": input("Enter quiz answer: "),
        "options": input("Enter quiz options (comma-separated): ").split(","),
    }

    # Send a POST request to create the quiz
    response = requests.post(API_URL, json=quiz)

    # Check if the quiz was created successfully
    if response.status_code == 201:
        print("Quiz created successfully!")
    else:
        print("Failed to create quiz")


def get_quiz_by_id():
    """
    Retrieve and print a quiz by its ID.

    Prompts the user to enter the quiz ID.
    Sends a GET request to the API to retrieve the quiz.
    Prints the quiz's ID, question, answer, and options if found.

    Raises:
        HTTPError: If the request fails or the quiz is not found.

    Prints:
        str: A formatted string with the quiz details or an error message.
    """
    # Prompt the user to enter the quiz ID
    quiz_id = int(input("Enter quiz ID: "))

    # Send a GET request to the API to retrieve the quiz by ID
    response = requests.get(f"{API_URL}/{quiz_id}")

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        quiz = response.json()
        # Return the quiz details as a formatted string
        print(json.dumps(quiz, indent=4))
    else:
        # Return an error message if the quiz was not found
        print("Quiz not found")


def update_quiz():
    """
    Update an existing quiz using user input.

    Prompts the user to enter the quiz ID and new details (question, answer, options).
    Sends a PATCH request to the API to update the quiz.

    Raises:
        HTTPError: If the request fails or the quiz is not found.

    Prints:
        str: A message indicating whether the update was successful or not.
    """
    # Send a GET request to the API to retrieve all quizzes
    response = requests.get(API_URL)
    # Prompt the user to enter the quiz ID
    quiz_id = int(input("Enter quiz ID: "))

    # Check if the request to get all quizzes was successful
    if response.status_code == 200:
        # Parse the JSON response
        quizzes = response.json()
        # Iterate through each quiz to find the matching ID
        for quiz in quizzes:
            if quiz["id"] == quiz_id:
                # Call the _update function to update the quiz
                return _update(quiz_id)
        print("Quiz not found")
    else:
        print("Failed to retrieve quizzes")


def _update(quiz_id: int):
    """
    Update the quiz with the given ID using user input.

    Prompts the user to enter new details (question, answer, options).
    Sends a PATCH request to the API to update the quiz.

    Args:
        quiz_id (int): The ID of the quiz to update.

    Prints:
        str: A message indicating whether the update was successful or not.
    """
    # Collect new quiz details from user input
    update_data = {
        "question": input("Enter new quiz question: "),
        "answer": input("Enter new quiz answer: "),
        "options": input("Enter new quiz options (comma-separated): ").split(","),
    }
    # Send a PATCH request to update the quiz
    response = requests.patch(f"{API_URL}/{quiz_id}", json=update_data)
    # Check if the quiz was updated successfully
    if response.status_code == 202:
        print("Quiz updated successfully!")
    else:
        print("Failed to update quiz")


def delete_quiz():
    """
    Delete a quiz by its ID.

    Prompts the user to enter the quiz ID.
    Sends a DELETE request to the API to delete the quiz.

    Raises:
        HTTPError: If the request fails or the quiz is not found.

    Prints:
        str: A message indicating whether the quiz was deleted successfully or not.
    """
    # Prompt the user to enter the quiz ID
    quiz_id = int(input("Enter quiz ID: "))

    # Send a DELETE request to delete the quiz by ID
    response = requests.delete(f"{API_URL}/{quiz_id}")

    # Check if the quiz was deleted successfully
    if response.status_code == 204:
        print("Quiz deleted successfully!")
    else:
        print("Failed to delete quiz")
