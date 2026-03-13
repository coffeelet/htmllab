# HTML Lab

HTML Lab is a Django-based web server simulator designed for teaching HTML, CSS, and JavaScript. It serves static files directly from a `www/` directory, mimicking a simple web server environment without the need for database configuration.

## Project Overview

*   **Type:** Django Web Application (Simulator)
*   **Purpose:** Educational tool for learning web development basics.
*   **Core Logic:**
    *   **Static Serving:** `htmllab/views.py` defines `StaticFileView` which serves files from `www/` and `htmllab/static/`.
    *   **Management Interface:** A `/manage/` route provides a GUI to preview and navigate pages within an iframe, with automatic link rewriting to keep navigation within the management context.
    *   **CLI Tools:** Custom management commands to scaffold new pages.

## Tech Stack

*   **Backend:** Python (3.10+), Django (6.x)
*   **Frontend Libraries:** Bootstrap 5, jQuery 4.0.0 (included in `htmllab/static/`)
*   **Database:** SQLite (configured but unused by the core logic)

## Key Files & Directories

*   `manage.py`: Django's command-line utility.
*   `htmllab/`: Project configuration and core logic.
    *   `settings.py`: Configuration. Defines `WWW_DIR` and `STATIC_DIR`.
    *   `urls.py`: Routing. Handles `/manage/`, `/guide/`, and catch-all static serving.
    *   `views.py`: Logic for serving files and rendering the management interface.
    *   `management/commands/createpage.py`: Implementation of the `createpage` command.
*   `www/`: **User Content Directory.** All user-created HTML, CSS, and JS files go here.
    *   `index.html`: The default homepage.
*   `htmllab/static/`: System static files.
    *   `base.html`: Template used by `createpage`.

## Building and Running

### Prerequisites

*   Python 3.10+

### Setup

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    # OR for development tools
    pip install -r requirements-dev.txt
    ```

### Development Server

Start the server:
```bash
python manage.py runserver
```
*   **Public View:** http://127.0.0.1:8000/ (Serves `www/index.html`)
*   **Management View:** http://127.0.0.1:8000/manage/

### Common Commands

**Create a New Page:**
Generates a new HTML file in `www/` based on `htmllab/static/base.html`.
```bash
python manage.py createpage mypage --title "My Page Title"
```

**Run Tests:**
```bash
python manage.py test
```

## Development Conventions

*   **Static Files:**
    *   User content belongs in `www/`.
    *   System/Library content belongs in `htmllab/static/`.
*   **Security:** `StaticFileView` explicitly checks that requested paths resolve within the allowed directories (`WWW_DIR` or `STATIC_DIR`) to prevent directory traversal.
*   **Templating:** The project uses Django templates for the management interface but serves user HTML files as static content (with optional link rewriting in the management view).
