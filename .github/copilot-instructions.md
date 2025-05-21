# Copilot Instructions

# This is a set of instructions for Copilot to follow when generating code.

# The instructions are designed to help Copilot understand the context and requirements of the code being generated.

# The instructions are divided into sections, each with a specific purpose.

# The sections are as follows:
1. General Instructions
2. Code Generation Instructions
3. Code Review Instructions
4. Code Refactoring Instructions
5. Code Documentation Instructions
6. Code Testing Instructions

# 1. General Instructions
- This project is a simple Flask web application.
- The main application logic is in `app/app.py`.
- HTML templates are stored in `app/templates/`.
- Python dependencies are listed in `app/requirements.txt`.
- GitHub Actions workflows are located in `.github/workflows/`.
- Pay attention to existing code patterns and style.

# 2. Code Generation Instructions
- When generating Python code, ensure it is compatible with Python 3.10.
- For Flask routes, follow the existing pattern in `app/app.py`.
- New HTML content should be placed in the `app/templates/` directory.
- If new Python dependencies are added, update `app/requirements.txt`.
- Ensure any new Flask routes render an HTML template.

# 3. Code Review Instructions
- Check for adherence to Flask best practices.
- Ensure HTML is well-formed and uses semantic tags where appropriate.
- Verify that any changes to `app/requirements.txt` are justified.
- Review GitHub Actions workflows for correctness and efficiency.
- Ensure code is readable and maintainable.

# 4. Code Refactoring Instructions
- Prioritize clarity and simplicity.
- Ensure refactored code maintains existing functionality.
- If refactoring affects dependencies, update `app/requirements.txt`.
- Consider performance implications of refactoring.

# 5. Code Documentation Instructions
- Add docstrings to new Python functions and classes.
- Comment complex or non-obvious code sections.
- Update the `README.md` if significant changes are made to the project structure or functionality.
- Ensure comments are clear, concise, and up-to-date.

# 6. Code Testing Instructions
- When adding new features, consider how they can be tested.
- If new backend functionality is added, update or add tests in the GitHub Actions workflow (`.github/workflows/test-app.yaml`) to verify the application starts and key endpoints are reachable.
- Tests should be simple and focus on core functionality.