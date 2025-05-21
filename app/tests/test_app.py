import pytest
from flask import template_rendered
from contextlib import contextmanager

@contextmanager
def captured_templates(app):
    """Context manager to capture templates being rendered."""
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
    assert app is not None

def test_hello_route(client):
    """Test that the hello route returns a 200 status code."""
    response = client.get('/')
    assert response.status_code == 200

def test_hello_route_renders_index_template(app, client):
    """Test that the hello route renders the index.html template."""
    with captured_templates(app) as templates:
        response = client.get('/')
        assert response.status_code == 200
        assert len(templates) == 1
        template, context = templates[0]
        assert template.name == 'index.html'