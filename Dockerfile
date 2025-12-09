# Use official Python runtime as base image
# Python 3.14 slim is smaller and faster than full Python
FROM python:3.12.12-slim

# Set working directory inside container - this is usually /app
WORKDIR /ai-ml-learning

ENV PYTHONPATH=/ai-ml-learning

# Install uv for faster dependency management
RUN pip install --no-cache-dir uv
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen # installs dev + main deps

#configures Unicorn server to run
CMD ["uv", "run", "--", "uvicorn", "concepts.month1.week2.src.fast_api.books:books_app", "--host", "0.0.0.0", "--reload"]



