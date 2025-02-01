import requests
from googleapiclient.discovery import build
from datetime import datetime, timedelta
from typing import Optional

# API Keys (Store securely in env variables for production)
GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
SEARCH_ENGINE_ID = "YOUR_SEARCH_ENGINE_ID"

YOUTUBE_API_KEY = 'AIzaSyA6jqg8S-vvwbvnJCGyv7-n6al0qC6W8jQ'
DEFAULT_RESULTS = 5


class StudyFetchService:
    def __init__(self):
        self.youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

    def search_youtube(self, subject: str, years_ago: Optional[int] = None, max_results: int = DEFAULT_RESULTS):
        published_after = None
        if years_ago is not None: #Converts number of years into youtube API Format (ISO 8601)
            past_date = datetime.utcnow() - timedelta(days=years_ago * 365)
            published_after = past_date.strftime("%Y-%m-%dT%H:%M:%SZ")

        # Prepare request parameters
        request_params = {
            "q": subject,
            "part": "snippet",
            "type": "video",
            "maxResults": max_results or NUMBER_OF_RESULTS,
            "order": "relevance",
            "relevanceLanguage": "en",
        }

        if published_after:
            request_params["publishedAfter"] = published_after

        request = self.youtube.search().list(**request_params)
        response = request.execute()

        #print(response)
        results = [
            {
                "title": item["snippet"]["title"],
                "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}",
                "published_at": item["snippet"]["publishedAt"]
            }
            for item in response.get("items", [])
        ]

        return results

    def search_practice_problems(self, subject: str, max_results: int = DEFAULT_RESULTS):

        return None
