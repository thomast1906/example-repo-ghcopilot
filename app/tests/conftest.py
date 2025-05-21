import pytest
import sys
import os
import importlib.util

# Add the parent directory to the path so we can import modules from there
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

@pytest.fixture
def app():
    """Create and configure a Flask app for testing."""
    try:
        from app import app as flask_app
    except ImportError:
        pytest.skip("Flask is not installed. Skipping tests that require Flask.")
        return None
    
    # Set testing configuration
    flask_app.config.update({
        "TESTING": True,
    })
    
    yield flask_app

@pytest.fixture
def client(app):
    """Create a test client for the app."""
    if app is None:
        pytest.skip("Flask app could not be created. Skipping.")
    return app.test_client()

@pytest.fixture
def runner(app):
    """Create a test CLI runner for the app."""
    if app is None:
        pytest.skip("Flask app could not be created. Skipping.")
    return app.test_cli_runner()

@pytest.fixture
def client(app):
    """Create a test client for the app."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """Create a test CLI runner for the app."""
    return app.test_cli_runner()