# Trivio - Quiz Management API

Trivio is a simple API to manage quizzes. It allows you to create, read, update, and delete quizzes. The API is built using FastAPI and provides endpoints to interact with quiz data stored in a JSON file.

## Features

- **Create a new quiz**  – Add new quiz questions with options and the correct answer.
- **Retrieve all quizzes** – Fetch all available quizzes from dataset.
- **Retrieve a quiz by its ID** – Fetch a specific quiz by its unique ID.
- **Update an existing quiz** – Modify an existing quiz's question, options, or answer.
- **Delete a quiz** – Remove a quiz from the dataset.

## API Endpoints

### 1. Get All Quizzes

- **Method**: `GET`
- **URL**: `/api/v1/quizzes`
- **Response**: A list of all quizzes. If no quizzes exist, returns an empty list.
- **Example Response**:

  ```json
  [
    {
      "id": 1,
      "question": "What is the capital of Canada?",
      "options": ["Ottawa", "Toronto", "Vancouver"],
      "answer": "Ottawa"
    },
    {
      "id": 2,
      "question": "Which gas is most abundant in Earth's atmosphere?",
      "options": ["Oxygen", "Nitrogen", "Carbon Dioxide"],
      "answer": "Nitrogen"
    }
  ]

### 3. Create a New Quiz

- **Method**: `POST`
- **URL**: `/api/v1/quizzes`
- **Request Body**:

  ```json
  {
    "id": 4,
    "question": "What is the capital of Japan?",
    "options": ["Tokyo", "Seoul", "Beijing", "Bangkok"],
    "answer": "Tokyo"
  }

- **Response**: A success message if the quiz is created successfully.

### 2. Get a Quiz by ID

- **Method**: `GET`
- **URL**: `/api/v1/quizzes/{id}`
- **Response**: The quiz data if found. If the quiz is not found, returns a 404 error.
- **Example Response**:

  ```json
  {
    "id": 1,
    "question": "What is the capital of Canada?",
    "options": ["Ottawa", "Toronto", "Vancouver"],
    "answer": "Ottawa"
  }


### 4. Update a Quiz

- **Method**: `PATCH`
- **URL**: `/api/v1/quizzes/{id}`
- **Request Body**:

  ```json
  {
    "question": "What is the largest planet in our solar system?",
    "options": ["Jupiter", "Saturn", "Neptune"],
    "answer": "Jupiter"
  }

- **Response**: A success message if the quiz is updated successfully. If the quiz is not found, returns a 404 error.

### 5. Delete a Quiz

- **Method**: `DELETE`
- **URL**: `/api/v1/quizzes/{id}`
- **Response**: A success message if the quiz is deleted successfully. If the quiz is not found, returns a 404 error.

## Running the Project

### Prerequisites

- Python 3.12+
- uv (Python package installer)

### Installation

- Clone the repository:

  ```bash
  git clone https://github.com/xpembe/trivio.git
  cd trivio
  ```

- Create a virtual environment and activate it:

  ```bash
  pip install uv
  uv add ruff
  source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
  ```

- Install the dependencies:

  ```bash
  uv pip install -r requirements.txt 
  ```

### Running the Server

- Start the FastAPI server:

  ```bash
  fastapi dev app/api/ 
  ```

The server will start running at <http://localhost:8000>.

### Running the CLI

- Ensure the server is running as described above.
- Open a new terminal and navigate to the src directory:

  ```bash
  cd src
  ```

- Run the CLI:

  ```bash
  python src/main.py
  ```

The CLI will provide options to interact with the API, such as getting all quizzes, creating a new quiz, getting a quiz by ID, updating a quiz, and deleting a quiz.

## Project Structure

  ```bash
  trivio/
  ├── .venv/
  ├── app/
  │   ├── api/
  │   │   ├── __init__.py
  │   │   ├── database.py
  │   │   ├── routes.py
  │   │   └── schemas.py
  │   └── __init__.py
  ├── src/
  │   └── main.py
  ├── .gitignore
  ├── python-version
  ├── quizzes.json
  ├── requirements.txt
  ├── uv.lock
  └── README.md
  ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
