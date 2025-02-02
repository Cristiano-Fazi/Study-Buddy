import requests
from googleapiclient.discovery import build
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch API Keys from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
DEFAULT_RESULTS = 5
DEFAULT_YEARS_AGO = 10
DEFAULT_VIDEO_LENGTH = 21

class StudyFetchService:
    def __init__(self):
        self.youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

    def search_youtube(self, subject: str, years_ago: int = DEFAULT_YEARS_AGO, max_results: int = DEFAULT_RESULTS, video_length: int = DEFAULT_VIDEO_LENGTH):
        published_after = None
        if years_ago is not None: #Converts number of years into youtube API Format (ISO 8601)
            past_date = datetime.utcnow() - timedelta(days=years_ago * 365)
            published_after = past_date.strftime("%Y-%m-%dT%H:%M:%SZ")

        # Determine the video duration filter
        video_duration = None
        if video_length <= 4:  # Short videos (less than 4 minutes)
            video_duration = "short"
        elif video_length > 4 and video_length < 20:  # Medium videos (4 to 20 minutes)
            video_duration = "medium"
        else:  # Long videos (more than 20 minutes)
            video_duration = "long"

        # Prepare request parameters
        request_params = {
            "q": subject,
            "part": "snippet",
            "type": "video",
            "maxResults": max_results or NUMBER_OF_RESULTS,
            "video_length": video_duration,
            "order": "relevance",
            "relevanceLanguage": "en",
        }

        if published_after:
            request_params["publishedAfter"] = published_after

        request = self.youtube.search().list(**request_params)
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

    def search_practice_problems(self, subject: str,years_ago: int = DEFAULT_YEARS_AGO, max_results: int = DEFAULT_RESULTS):
        query = f"{subject} (practice problems OR exercises) filetype:pdf site:.edu OR site:khanacademy.org OR site:ocw.mit.edu"
        
        # Google Custom Search API URL
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={GOOGLE_API_KEY}&cx={SEARCH_ENGINE_ID}&num={max_results}&lr=lang_en"

        # Execute the API request
        response = requests.get(url).json()

        # Extract relevant results
        return [
            {
                "title": item.get("title"),
                "url": item.get("link"),
                "snippet": item.get("snippet"),
            }
            for item in response.get("items", [])
        ]

    def search_exams(self, subject: str,years_ago: int = DEFAULT_YEARS_AGO, max_results: int = DEFAULT_RESULTS):
        query = f"{subject} (previous midterm exams OR final exams OR practice exams) filetype:pdf site:.edu OR site:khanacademy.org OR site:ocw.mit.edu"
        
        # Google Custom Search API URL
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={GOOGLE_API_KEY}&cx={SEARCH_ENGINE_ID}&num={max_results}&lr=lang_en"

        # Execute the API request
        response = requests.get(url).json()

        # Extract relevant results
        return [
            {
                "title": item.get("title"),
                "url": item.get("link"),
                "snippet": item.get("snippet"),
            }
            for item in response.get("items", [])
        ]
