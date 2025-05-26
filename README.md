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
└── README.md                # This file
```

## Dependencies

The application uses the following Python packages:
- Flask 2.0.0 - Web framework
- Werkzeug 2.0.0 - WSGI utility library

All dependencies can be installed using the requirements.txt file.

## Testing

The repository includes a GitHub Actions workflow that tests if the application starts correctly and responds to HTTP requests. To run tests locally:

1. Start the application as described in the "Running the Application" section
2. Use curl or a web browser to verify the application is responding:
   ```bash
   curl http://localhost:5000/
   ```

## License

See the LICENSE file for details (if available).
