import requests


# Base URL for the API endpoints
API_URL = "http://localhost:8000/api/v1/quizzes"


def get_all_quizzes():
    """
    Retrieve and print all quizzes from the API.

    Sends a GET request to the API to retrieve all quizzes.
    Prints each quiz's ID, question, answer, and options.

    Raises:
        HTTPError: If the request fails.
    """
    response = requests.get(API_URL)
    if response.status_code == 200:
        quizzes = response.json()
        for quiz in quizzes:
            print(
                f"ID: {quiz['id']}, Question: {quiz['question']}, Answer: {quiz['answer']}, Options: {quiz['options']}"
            )
    else:
        print("Failed to retrieve quizzes")


def create_quiz():
    """
    Create a new quiz using user input.

    Prompts the user to enter quiz details (ID, question, answer, options).
    Sends a POST request to the API to create the quiz.

    Raises:
        HTTPError: If the request fails.
    """
    quiz = {
        "id": int(input("Enter quiz ID: ")),
        "question": input("Enter quiz question: "),
        "answer": input("Enter quiz answer: "),
        "options": input("Enter quiz options (comma-separated): ").split(","),
    }
    response = requests.post(API_URL, json=quiz)
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
    """
    quiz_id = int(input("Enter quiz ID: "))
    response = requests.get(f"{API_URL}/{quiz_id}")
    if response.status_code == 200:
        quiz = response.json()
        print(
            f"ID: {quiz['id']}, Question: {quiz['question']}, Answer: {quiz['answer']}, Options: {quiz['options']}"
        )
    else:
        print("Quiz not found")


def update_quiz():
    """
    Update an existing quiz using user input.

    Prompts the user to enter the quiz ID and new details (question, answer, options).
    Sends a PATCH request to the API to update the quiz.

    Raises:
        HTTPError: If the request fails or the quiz is not found.
    """
    quiz_id = int(input("Enter quiz ID: "))
    update_data = {
        "question": input("Enter new quiz question: "),
        "answer": input("Enter new quiz answer: "),
        "options": input("Enter new quiz options (comma-separated): ").split(","),
    }
    response = requests.patch(f"{API_URL}/{quiz_id}", json=update_data)
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
    """
    quiz_id = int(input("Enter quiz ID: "))
    response = requests.delete(f"{API_URL}/{quiz_id}")
    if response.status_code == 204:
        print("Quiz deleted successfully!")
    else:
        print("Failed to delete quiz")


def main():
    """
    Main function to run the Quiz Management CLI.

    Displays a menu with options to get all quizzes, create a quiz, get a quiz by ID,
    update a quiz, delete a quiz, or exit the program.
    """
    while True:
        print("\nQuiz Management CLI\n")
        print("1. Get all quizzes")
        print("2. Create a new quiz")
        print("3. Get a quiz by ID")
        print("4. Update a quiz")
        print("5. Delete a quiz")
        print("6. Exit")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            get_all_quizzes()
        elif choice == "2":
            create_quiz()
        elif choice == "3":
            get_quiz_by_id()
        elif choice == "4":
            update_quiz()
        elif choice == "5":
            delete_quiz()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
