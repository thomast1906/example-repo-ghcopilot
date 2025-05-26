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
│   └── requirements.txt     # Python dependencies
├── tests/
│   ├── README.md            # Information about the tests
│   └── test_app.py          # Tests for the Flask application
├── pytest.ini               # Configuration for pytest
└── README.md                # This file
```

## Dependencies

The application uses the following Python packages:
- Flask 2.0.0 - Web framework
- Werkzeug 2.0.0 - WSGI utility library
- pytest 7.4.0 - Testing framework

All dependencies can be installed using the requirements.txt file.

## Testing

The repository includes automated tests using pytest and a GitHub Actions workflow that verifies the application works correctly. The tests check:

1. Application initialization
2. Home page returns correct status code (200)
3. Home page returns correct HTML content
4. Non-existent pages return 404 status code

To run tests locally:

1. Install the required dependencies:
   ```bash
   pip install -r app/requirements.txt
   ```

2. Run the tests:
   ```bash
   pytest
   ```
   
   For more verbose output:
   ```bash
   pytest -v
   ```

3. You can also manually test the application by starting it and using curl:
   ```bash
   cd app
   python app.py
   # In another terminal
   curl http://localhost:5000/
   ```

## License

See the LICENSE file for details (if available).
