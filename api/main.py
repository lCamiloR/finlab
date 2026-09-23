from fastapi import FastAPI
from models.search import SearchResponse, SearchRequest
from services.search import SearchService
from config.settings import settings

app = FastAPI(title="Financial Search API", version="1.0.0")

search_service = SearchService(
    qdrant_url=settings.qdrant_url,
    qdrant_api_key=settings.qdrant_api_key,
    collection_name=settings.collection_name,
)


@app.post("/search", response_model=SearchResponse)
def search(request: SearchRequest):
    return search_service.search(query=request.query, limit=request.limit)


@app.get("/")
def root():
    return {"message": "Welcome to the Financial Search API"}
