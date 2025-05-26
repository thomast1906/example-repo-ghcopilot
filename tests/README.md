# Flask Application Tests

This directory contains tests for the Flask web application.

## Test Cases

The tests verify the following functionality:

1. **Application Initialization**: Tests that the Flask application initializes correctly.
2. **Home Page Status Code**: Tests that the home page returns a 200 status code.
3. **Home Page Content**: Tests that the home page returns the correct HTML content.
4. **404 for Nonexistent Pages**: Tests that a 404 status code is returned for non-existent pages.

## Running Tests

To run the tests locally:

```bash
# Install dependencies
pip install -r app/requirements.txt

# Run tests
pytest
```

For more verbose output:

```bash
pytest -v
```