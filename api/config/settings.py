from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

finlab_root = Path(__file__).parents[2]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=f"{finlab_root}/.env",
        env_file_encoding="utf-8",
        extra="allow",
    )

    qdrant_url: str
    qdrant_api_key: str
    collection_name: str = "finlab"
    dense_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    sparser_model: str = "Qdrant/bm25"
    colbert_model: str = "colbert-ir/colbertv2.0"


settings = Settings()
