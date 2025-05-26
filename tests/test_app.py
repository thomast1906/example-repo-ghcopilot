import pytest
from app.app import app as flask_app


@pytest.fixture
def app():
    """Create and configure a Flask app for testing."""
    # Set testing mode to True
    flask_app.config.update({
        "TESTING": True,
    })
    yield flask_app


@pytest.fixture
def client(app):
    """Create a test client for the Flask app."""
    return app.test_client()


def test_app_initializes(app):
    """Test that the Flask application initializes correctly."""
    assert app is not None
    assert app.name == 'app.app'


def test_home_page_status_code(client):
    """Test that the home page returns a 200 status code."""
    response = client.get('/')
    assert response.status_code == 200


def test_home_page_content(client):
    """Test that the home page returns the correct HTML content."""
    response = client.get('/')
    assert b'Hello, World from thomasthornton.cloud' in response.data
    assert b'Explore DevOps the Hard Way Azure' in response.data


def test_404_for_nonexistent_page(client):
    """Test that a 404 status code is returned for a non-existent page."""
    response = client.get('/nonexistent-page')
    assert response.status_code == 404