# AGENTS.md - Coding Guidelines for HTML Lab

## Project Overview
Django 6.0.3 project that serves static files from a `www/` directory. Simple web server simulator without database requirements for static content.

## Build/Run Commands

```bash
# Run development server
python manage.py runserver

# Run with specific port
python manage.py runserver 8080

# Database migrations (when needed)
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Django shell
python manage.py shell
```

## Testing Commands

```bash
# Run all tests
python manage.py test

# Run specific test module
python manage.py test htmllab.tests

# Run single test class
python manage.py test htmllab.tests.StaticFileViewTest

# Run single test method
python manage.py test htmllab.tests.StaticFileViewTest.test_index_html

# Run with verbosity
python manage.py test --verbosity=2

# Run with coverage (install coverage first: pip install coverage)
coverage run --source='.' manage.py test
coverage report
coverage html
```

## Linting & Formatting

```bash
# Install tools
pip install flake8 black isort mypy

# Run flake8 (linting)
flake8 htmllab/

# Format with black
black htmllab/

# Sort imports with isort
isort htmllab/

# Type checking with mypy
mypy htmllab/

# Check all (run before commits)
flake8 htmllab/ && black --check htmllab/ && isort --check htmllab/
```

## Code Style Guidelines

### Imports
- Group imports: stdlib → third-party → Django → local
- Use absolute imports over relative imports
- Sort with isort (default config compatible with black)

```python
# Standard library
import mimetypes
from pathlib import Path

# Third-party
import requests  # if used

# Django
from django.conf import settings
from django.http import FileResponse, Http404
from django.views import View

# Local
from htmllab.utils import some_helper
```

### Formatting
- Follow PEP 8
- Use Black formatter (88 character line length)
- 4 spaces for indentation
- Two blank lines between top-level functions/classes
- One blank line between methods

### Naming Conventions
- Classes: `PascalCase` (e.g., `StaticFileView`)
- Functions/Methods: `snake_case` (e.g., `get_context_data`)
- Variables: `snake_case` (e.g., `file_path`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `MAX_FILE_SIZE`)
- Private attributes: `_leading_underscore`

### Type Hints
- Add type hints to function signatures
- Use `from __future__ import annotations` for Python 3.7+ compatibility

```python
from __future__ import annotations

def process_file(file_path: Path) -> FileResponse:
    ...
```

### Docstrings
- Use triple double quotes
- Chinese or English accepted (be consistent per module)
- First line: concise summary

```python
def get_file(self, path: str) -> FileResponse:
    """Retrieve static file from www directory.
    
    Args:
        path: Relative path to file
        
    Returns:
        FileResponse with appropriate content type
        
    Raises:
        Http404: If file not found or access denied
    """
```

### Error Handling
- Use Django's built-in exceptions (`Http404`, `PermissionDenied`)
- Use `try/except` for expected errors, avoid bare `except:`
- Always chain exceptions with `from` when re-raising

```python
try:
    file_path.resolve().relative_to(www_dir.resolve())
except ValueError as exc:
    raise Http404("Access denied") from exc
```

### Views
- Prefer class-based views (CBV) over function-based views (FBV)
- Keep views thin, move logic to models/managers/services
- Use Django's generic views when applicable

### Security
- Always validate user input paths (prevent directory traversal)
- Use `resolve()` and `relative_to()` for path validation
- Never expose sensitive settings or file system details in errors

### Static Files
- All static content served from `www/` directory
- Use `settings.WWW_DIR` for path references
- Set appropriate MIME types using `mimetypes.guess_type()`

## Pre-commit Checklist
- [ ] Tests pass: `python manage.py test`
- [ ] Code formatted: `black htmllab/`
- [ ] Imports sorted: `isort htmllab/`
- [ ] No lint errors: `flake8 htmllab/`
- [ ] Type hints added for new functions
- [ ] Docstrings updated
