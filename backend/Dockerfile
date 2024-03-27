# Use the official Python image
FROM python:3.12.2-slim as python-base

# Set environment variables
ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# `builder-base` stage is used to build deps + create our virtual environment
FROM python-base as builder-base
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential

# Install Poetry
RUN  curl -sSL https://install.python-poetry.org | python3 -

# Copy only the dependencies definition file
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

# Install poetry libraries
RUN poetry install --no-dev


# `development` image is used during development / testing
FROM python-base as development
ENV FASTAPI_ENV=development
WORKDIR $PYSETUP_PATH

# copy in our built poetry + venv
COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

# quicker install as runtime deps are already installed
RUN poetry install

# will become mountpoint of our code
WORKDIR /app
COPY . .

CMD ["/opt/pysetup/.venv/bin/poetry", "run", "uvicorn", "--port", "5000","--host", "0.0.0.0", "main:app"]
