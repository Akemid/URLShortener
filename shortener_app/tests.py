from fastapi.testclient import TestClient

from .config import Settings, get_settings
from .main import app

client = TestClient(app)


def get_settings_override():
    return Settings(app_name="Awesome API")


app.dependency_overrides[get_settings] = get_settings_override


def test_app():
    response = client.get("/info")
    data = response.json()
    assert data == {
        "app_name": "Awesome API",
        "env_name": "Local",
        "base_url": "http://localhost:8000",
        "db_url": "sqlite:///./shortener.db",
    }
