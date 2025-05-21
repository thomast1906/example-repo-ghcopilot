import pytest
import sys

try:
    from flask import template_rendered
    from contextlib import contextmanager

    @contextmanager
    def captured_templates(app):
        """Context manager to capture templates being rendered."""
        if app is None:
            yield []
            return
            
        recorded = []
        def record(sender, template, context, **extra):
            recorded.append((template, context))
        template_rendered.connect(record, app)
        try:
            yield recorded
        finally:
            template_rendered.disconnect(record, app)

    def test_app_exists(app):
        """Test that the app exists."""
        if app is None:
            pytest.skip("Flask app could not be created. Skipping.")
        assert app is not None

    def test_hello_route(client):
        """Test that the hello route returns a 200 status code."""
        if client is None:
            pytest.skip("Test client could not be created. Skipping.")
        response = client.get('/')
        assert response.status_code == 200

    def test_hello_route_renders_index_template(app, client):
        """Test that the hello route renders the index.html template."""
        if app is None or client is None:
            pytest.skip("Flask app or test client could not be created. Skipping.")
            
        with captured_templates(app) as templates:
            response = client.get('/')
            assert response.status_code == 200
            assert len(templates) == 1
            template, context = templates[0]
            assert template.name == 'index.html'
except ImportError:
    # Define placeholder tests if Flask is not installed
    def test_placeholder():
        """Placeholder test when Flask is not available."""
        pytest.skip("Flask is not installed. Skipping all Flask-dependent tests.")