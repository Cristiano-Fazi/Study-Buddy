from fastapi import FastAPI
from services.search_service import StudyFetchService
from typing import Optional

app = FastAPI()
study_fetch = StudyFetchService()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Study Buddy API!"}

@app.get("/youtube/{subject}/")
def youtube_endpoint(subject: str, years_ago: Optional[int] = None):
    """
    Endpoint to search YouTube videos by subject.
    - `subject`: Subject of video to search for.
    """
    return study_fetch.search_youtube(subject=subject)

@app.get("/youtube/{subject}/{years_ago}/")
def youtube_endpoint(subject: str, years_ago: Optional[int] = None):
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
def practice_endpoint(subject: str, years_ago: Optional[int] = None):
    """
    Searches the internet for PDF's relating to the given subject
    - `subject`: Subject of practice to search for.
    """
    return study_fetch.search_practice_problems(subject=subject)

@app.get("/practice/{subject}/{years_ago}/")
def practice_endpoint(subject: str, years_ago: Optional[int] = None):
    """
    Searches the internet for PDF's relating to the given subject
    - `subject`: Subject of practice to search for.
    - `years_ago`: Max amount of years ago the practice could have been published.
    """
    return study_fetch.search_practice_problems(subject=subject, years_ago=years_ago)

@app.get("/practice/{subject}/{years_ago}/{max_results}/")
def practice_endpoint(subject: str, years_ago: Optional[int] = None, max_results: Optional[int] = None):
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
