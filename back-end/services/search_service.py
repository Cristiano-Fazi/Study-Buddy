import requests
from googleapiclient.discovery import build
from datetime import datetime, timedelta

# API Keys (Store securely in env variables for production)
GOOGLE_API_KEY = "AIzaSyA6jqg8S-vvwbvnJCGyv7-n6al0qC6W8jQ"
SEARCH_ENGINE_ID = "f1933b0266ecd41d3"
YOUTUBE_API_KEY = 'AIzaSyA6jqg8S-vvwbvnJCGyv7-n6al0qC6W8jQ'
DEFAULT_RESULTS = 5
DEFAULT_YEARS_AGO = 10


class StudyFetchService:
    def __init__(self):
        self.youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

    def search_youtube(self, subject: str, years_ago: int = DEFAULT_YEARS_AGO, max_results: int = DEFAULT_RESULTS):
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
        # Search query: Includes subject, problem types, and filters for PDFs & educational sites
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
