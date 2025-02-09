from utils import get_all_quizzes, create_quiz
from utils import get_quiz_by_id, update_quiz, delete_quiz


def main():
    """
    Main function to run the Quiz Management CLI.

    Displays a menu with options to get all quizzes, create a quiz, get a quiz by ID,
    update a quiz, delete a quiz, or exit the program.
    """
    while True:
        # Print the CLI header
        print("\nQuiz Management CLI")
        # Print the menu options
        print(choices())
        # Prompt the user to enter their choice
        choice = input("\nEnter your choice: ")
        print()
        # Handle the user's choice
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
            # Print an error message for invalid choices
            print("Invalid choice. Please try again.")


def choices() -> str:
    """
    Returns a string representing the menu options for the Quiz Management CLI.

    The menu includes options to:
    1. Get all quizzes
    2. Create a new quiz
    3. Get a quiz by ID
    4. Update a quiz
    5. Delete a quiz
    6. Exit the program

    Returns:
        str: The menu options as a formatted string.
    """
    return """
    1. Get all quizzes 
    2. Create a new quiz
    3. Get a quiz by ID
    4. Update a quiz
    5. Delete a quiz
    6. Exit"""


if __name__ == "__main__":
    main()
