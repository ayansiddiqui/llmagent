import os
import sys
from unittest.mock import AsyncMock

os.environ.setdefault("OPENAI_API_KEY", "test")
sys.path.insert(0, os.path.abspath("./src"))

from fastapi.testclient import TestClient
from llmagent.api.api import app, service

# Mock OpenAI client to avoid real API call
service.client.generate_response = AsyncMock(return_value="ok")

client = TestClient(app)

def test_chat_endpoint():
    response = client.post('/chat', json={'user': 'test', 'content': 'hello'})
    assert response.status_code == 200
    assert response.json()['response'] == 'ok'
