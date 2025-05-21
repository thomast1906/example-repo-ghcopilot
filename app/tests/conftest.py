import pytest
from app import app as flask_app

@pytest.fixture
def app():
    """Create and configure a Flask app for testing."""
    # Set testing configuration
    flask_app.config.update({
        "TESTING": True,
    })
    
    yield flask_app

@pytest.fixture
def client(app):
    """Create a test client for the app."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """Create a test CLI runner for the app."""
    return app.test_cli_runner()