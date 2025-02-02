from fastapi import FastAPI
from services.search_service import StudyFetchService
from typing import Optional
from services.gen_ai_service import gen_ai_call_async
from fastapi.middleware.cors import CORSMiddleware
import asyncio

app = FastAPI()
study_fetch = StudyFetchService()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, or specify your frontend URL here
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Study Buddy API!"}

@app.get("/youtube/{subject}/")
def youtube_endpoint(subject: str):
    """
    Endpoint to search YouTube videos by subject.
    - `subject`: Subject of video to search for.
    """
    return study_fetch.search_youtube(subject=subject)

@app.get("/youtube/{subject}/{years_ago}/")
def youtube_endpoint(subject: str, years_ago: int):
    """
    Endpoint to search YouTube videos by subject.
    - `subject`: Subject of video to search for.
    - `years_ago`: Max amount of years ago the video could have been published.
    """
    if years_ago is not None and years_ago < 0:
        return {"error": "years_ago must be a positive integer or null"}
    
    return study_fetch.search_youtube(subject=subject, years_ago=years_ago)

@app.get("/youtube/{subject}/{years_ago}/{max_results}/")
def youtube_endpoint(subject: str, years_ago: int, max_results: int):
    """
    Endpoint to search YouTube videos by subject.
    - `subject`: Subject of video to search for.
    - `years_ago`: Max amount of years ago the video could have been published.
    - `max_results`: The number of videos that will be returned.
    """
    if years_ago is not None and years_ago < 0:
        return {"error": "years_ago must be a positive integer or null"}
    
    if max_results is not None and max_results < 0:
        return {"error": "max_results must be a positive integer or null"}
    
    return study_fetch.search_youtube(subject=subject, years_ago=years_ago, max_results=max_results)

@app.get("/practice/{subject}/")
def practice_endpoint(subject: str):
    """
    Searches the internet for PDF's relating to the given subject
    - `subject`: Subject of practice to search for.
    """
    return study_fetch.search_practice_problems(subject=subject)

@app.get("/practice/{subject}/{years_ago}/")
def practice_endpoint(subject: str, years_ago: int):
    """
    Searches the internet for PDF's relating to the given subject
    - `subject`: Subject of practice to search for.
    - `years_ago`: Max amount of years ago the practice could have been published.
    """
    return study_fetch.search_practice_problems(subject=subject, years_ago=years_ago)

@app.get("/practice/{subject}/{years_ago}/{max_results}/")
def practice_endpoint(subject: str, years_ago: int, max_results: int):
    """
    Searches the internet for PDF's relating to the given subject
    - `subject`: Subject of practice to search for.
    - `years_ago`: Max amount of years ago the practice could have been published.
    - `max_results`: The number of videos that will be returned.
    """
    if years_ago is not None and years_ago < 0:
        return {"error": "years_ago must be a positive integer or null"}
    
    if max_results is not None and max_results < 0:
        return {"error": "max_results must be a positive integer or null"}

    return study_fetch.search_practice_problems(subject=subject, years_ago=years_ago, max_results=max_results)

@app.get("/exam/{subject}/")
def exam_endpoint(subject: str):
    """
    Searches the internet for PDF's relating to the given subject
    - `subject`: Subject of practice to search for.
    """
    return study_fetch.search_exams(subject=subject)

@app.get("/exam/{subject}/{years_ago}/")
def exam_endpoint(subject: str, years_ago: int):
    """
    Searches the internet for PDF's relating to the given subject
    - `subject`: Subject of practice to search for.
    - `years_ago`: Max amount of years ago the practice could have been published.
    """
    return study_fetch.search_exams(subject=subject, years_ago=years_ago)

@app.get("/exam/{subject}/{years_ago}/{max_results}/")
def exam_endpoint(subject: str, years_ago: int, max_results: int):
    """
    Searches the internet for PDF's relating to the given subject
    - `subject`: Subject of practice to search for.
    - `years_ago`: Max amount of years ago the practice could have been published.
    - `max_results`: The number of videos that will be returned.
    """
    if years_ago is not None and years_ago < 0:
        return {"error": "years_ago must be a positive integer or null"}
    
    if max_results is not None and max_results < 0:
        return {"error": "max_results must be a positive integer or null"}

    return study_fetch.search_exams(subject=subject, years_ago=years_ago, max_results=max_results)

# Text will be too long no?
@app.get("/chat/{subject}/")
async def ai_chat_endpoint(subject: str):
    """
    Generates an explanation of what the subject is using generative AI.
    - `subject`: Subject to be explained.
    """
    print("Hitting the endpoint")
    return await gen_ai_call_async(subject)
