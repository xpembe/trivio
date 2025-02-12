from fastapi import FastAPI
from contextlib import asynccontextmanager

from .api import routes
from .db.database import init_db

# Define the version of the API
VERSION = "v1"


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server is starting...")
    await init_db()
    yield
    print("Server has been stopped")


# Create an instance of FastAPI
app = FastAPI(
    title="Quiz API",  # Title of the API
    version=VERSION,  # Version of the API
    description="A simple API to manage quizzes.",  # Description of the API
    lifespan=lifespan,
)

# Include the router from the routes module
app.include_router(
    router=routes.router,  # The router to include
    prefix=f"/api/{VERSION}/quizzes",  # Prefix for all routes in this router
    tags=["quizzes"],  # Tags for the routes in this router
)
