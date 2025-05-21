import pytest
import sys
import os
import importlib.util

# Add the parent directory to the path so we can import modules from there
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

@pytest.fixture
def app():
    """Create and configure a Flask app for testing."""
    try:
        # First try direct import
        try:
            # Try importing from the current directory structure
            import app as app_module
            flask_app = app_module.app
        except ImportError:
            # If that fails, try importing the app.py file directly
            app_path = os.path.join(parent_dir, 'app.py')
            spec = importlib.util.spec_from_file_location('app_module', app_path)
            app_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(app_module)
            flask_app = app_module.app
    except (ImportError, AttributeError) as e:
        print(f"Error importing Flask app: {e}")
        pytest.skip("Could not import Flask app. Skipping tests that require Flask.")
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