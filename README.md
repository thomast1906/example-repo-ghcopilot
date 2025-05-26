# Example Repository - GitHub Copilot

A simple Flask web application to showcase GitHub Copilot functionality. This application serves a basic "Hello World" webpage with styling.

## Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/thomast1906/example-repo-ghcopilot.git
   cd example-repo-ghcopilot
   ```

2. Install the required dependencies:
   ```bash
   pip install -r app/requirements.txt
   ```

## Running the Application

1. Navigate to the app directory:
   ```bash
   cd app
   ```

2. Start the Flask application:
   ```bash
   python app.py
   ```

3. The application will run on `http://0.0.0.0:5000` by default. Open your browser and navigate to this address to view the application.

   Note: You can change the port by setting the `PORT` environment variable before running the application.

## Project Structure

```
example-repo-ghcopilot/
├── .github/
│   └── workflows/
│       └── test-app.yaml    # GitHub Actions workflow for testing
├── app/
│   ├── templates/
│   │   └── index.html       # HTML template for the web application
│   ├── app.py               # Main Flask application code
│   ├── requirements.txt     # Python dependencies
│   └── requirements-dev.txt # Python development dependencies
├── tests/
│   ├── conftest.py          # Pytest configuration
│   └── test_app.py          # Tests for the Flask application
└── README.md                # This file
```

## Dependencies

The application uses the following Python packages:
- Flask 2.0.0 - Web framework
- Werkzeug 2.0.0 - WSGI utility library

Development dependencies:
- pytest - Testing framework
- pytest-flask - Flask plugin for pytest

All dependencies can be installed using the requirements.txt and requirements-dev.txt files.

## Testing

The repository includes automated tests using pytest and a GitHub Actions workflow that verifies the application functionality. The tests check:

1. Application startup and response
2. Home page returns correct status code (200)
3. Home page contains expected content
4. Proper 404 handling for non-existent pages

To run tests locally:

1. Install the development dependencies:
   ```bash
   pip install -r app/requirements-dev.txt
   ```

2. Run the tests using pytest:
   ```bash
   python -m pytest tests/
   ```

You can also manually verify the application:
1. Start the application as described in the "Running the Application" section
2. Use curl or a web browser to verify the application is responding:
   ```bash
   curl http://localhost:5000/
   ```

## License

See the LICENSE file for details (if available).
