import pytest
import os
import sys

# Add the app directory to the path so we can import app.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

from app import app

@pytest.fixture
def client():
    """Create a test client for the app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that the home page returns a 200 status code."""
    response = client.get('/')
    assert response.status_code == 200

def test_home_page_content(client):
    """Test that the home page contains expected HTML content."""
    response = client.get('/')
    assert b'Hello, World from thomasthornton.cloud' in response.data
    assert b'DevOps the Hard Way' in response.data
    assert b'Start Learning' in response.data

def test_404_page(client):
    """Test that accessing a non-existent page returns a 404 status code."""
    response = client.get('/nonexistent-page')
    assert response.status_code == 404