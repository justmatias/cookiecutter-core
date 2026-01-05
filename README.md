# Cookiecutter Core

A production-ready Cookiecutter template for modern Python projects with Ruff, Pylint, MyPy, and poethepoet configuration.

## Usage

1. Install `cookiecutter` if you haven't already:

    ```bash
    pip install cookiecutter
    ```

2. Generate a new project using this template:

    ```bash
    cookiecutter https://github.com/matiagimenez/cookiecutter-in-agentic-mode
    # OR if you have it locally
    cookiecutter .
    ```

3. Follow the prompts to configure your project.

## Template Options

*   `project_name`: The name of your project (Human readable).
*   `project_slug`: The directory name for your project (default is dash-separated `project_name`).
*   `module_name`: The python package name (default is snake_case `project_slug`).
*   `short_description`: A short description of the project.
*   `author_name`: Your name.
*   `author_email`: Your email.
*   `version`: Initial version.
*   `python_version`: Python version to support.

## Features

*   **Poetry/UV** friendly structure (uses `pyproject.toml`).
*   **Ruff, Pylint, MyPy** configured.
*   **poethepoet** task runner configured.
