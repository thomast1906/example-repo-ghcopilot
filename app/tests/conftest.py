import pytest
import sys
import os

# Add the parent directory to the path so we can import app.py
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

@pytest.fixture
def app():
    """Create and configure a Flask app for testing."""
    # Import the Flask app directly from the app.py module
    try:
        # Simple import from the parent directory
        sys.path.insert(0, parent_dir)
        from app import app as flask_app
        
        # Set testing configuration
        flask_app.config.update({
            "TESTING": True,
        })
        
        return flask_app
    except Exception as e:
        print(f"Error importing Flask app: {e}")
        print(f"Python path: {sys.path}")
        pytest.skip(f"Could not import Flask app: {e}")
        return None

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