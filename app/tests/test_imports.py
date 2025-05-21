import os
import sys

# Print current directory for debugging
print("Current directory:", os.getcwd())
print("Directory content:", os.listdir('.'))
print("sys.path:", sys.path)

# Try to manually import app module
try:
    sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
    from app import app
    print("Successfully imported app:", app)
except Exception as e:
    print("Error importing app:", str(e))