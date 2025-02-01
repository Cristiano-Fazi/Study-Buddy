from fastapi import FastAPI
from googleapiclient.discovery import build
from datetime import datetime, timedelta
from typing import Optional

app = FastAPI()
YOUTUBE_API_KEY = 'AIzaSyDrUt7hEEmzXQ3wTlgZ2H3Epp57bVWPhbQ'#Old Key
YOUTUBE_API_KEY = 'AIzaSyA6jqg8S-vvwbvnJCGyv7-n6al0qC6W8jQ'

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/dummy")
def dummy_endpoint():
    return {"message": "This is a dummy endpoint"}

@app.get("/youtube/{subject}/{years_ago}/")
def youtube_endpoint(subject: str, years_ago: Optional[int] = None):
    if years_ago is not None and years_ago < 0:
        return {"error": "years_ago must be a positive integer or null"}
    
    return search_youtube(subject, years_ago=years_ago)


def search_youtube(subject, years_ago: Optional[int] = None, max_results: Optional[int] = None):
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

    published_after = None
    if years_ago is not None:
        past_date = datetime.utcnow() - timedelta(days=years_ago * 365)
        published_after = past_date.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Prepare request parameters
    request_params = {
        "q": subject,
        "part": "snippet",
        "type": "video",
        "maxResults": max_results,
        "order": "date"  # Newest videos first
    }

    if published_after:
        request_params["publishedAfter"] = published_after

    request = youtube.search().list(**request_params)
    response = request.execute()

    results = [
        {
            "title": item["snippet"]["title"],
            "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}",
            "published_at": item["snippet"]["publishedAt"]
        }
        for item in response.get("items", [])
    ]

    return results