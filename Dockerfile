FROM mcr.microsoft.com/devcontainers/python:0-3.10
RUN pipx install poetry
ADD pyproject.toml .
ADD poetry.lock .
RUN poetry config virtualenvs.create false
RUN poetry config installer.max-workers 10
RUN poetry install --no-root
