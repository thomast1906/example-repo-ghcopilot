import pytest
import os
import sys

# Add the app directory to the path so we can import app.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))