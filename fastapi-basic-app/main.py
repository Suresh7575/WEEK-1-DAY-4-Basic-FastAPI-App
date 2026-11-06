
from fastapi import FastAPI
from pydantic import BaseModel


# ======================== FastAPI Application ========================

app = FastAPI(
    title="Basic FastAPI App",
    description="A simple web API built for Assignment 4",
    version="1.0.0"
)


# ======================== Pydantic Models ========================

class WelcomeResponse(BaseModel):
    message: str


class GreetingResponse(BaseModel):
    name: str
    message: str


# ======================== API Routes ========================

# Root endpoint
@app.get("/", response_model=WelcomeResponse)
def home():
    return {
        "message": "Hello, FastAPI"
    }


# Greeting endpoint with path parameter
@app.get("/greet/{name}", response_model=GreetingResponse)
def greet_user(name: str):
    return {
        "name": name,
        "message": f"Hello, {name}! Welcome to FastAPI."
    }