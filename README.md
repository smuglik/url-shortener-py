# URL Shortener

A modern, fast, and scalable URL shortening service built with Python, FastAPI, and PostgreSQL.

## Features

- Create short URLs from long URLs
- Redirect to original URLs using short codes
- PostgreSQL database for persistent storage
- FastAPI for high-performance API endpoints
- Docker support for easy deployment
- Type hints and comprehensive code quality checks
- Alembic for database migrations

## Tech Stack

- Python 3.13+
- FastAPI
- PostgreSQL 17
- SQLAlchemy
- Alembic
- Docker & Docker Compose
- Ruff for linting and formatting

## Prerequisites

- Python 3.13 or higher
- Docker and Docker Compose
- UV package manager (recommended)
- Taskfile

## Getting Started

1. Clone the repository:
2. Create and activate a virtual environment:
```bash
uv sync
source .venv/bin/activate # On Unix/macOS
# or
.venv\Scripts\activate # On Windows
```

3. Start the PostgreSQL database:
```bash
task start-db
```

4. Run database migrations:
```bash
task migrate
```

6. Start the application:

- Development server
```bash
task run-dev
```
- Production server
```bash
task run-prod
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Create Short URL
```http
POST /shorten
Content-Type: application/json

{
    "url": "https://example.com/very/long/url"
}
```

Response:
```json
{
    "short_url": "generated_short_code",
    "created_at": "2024-03-21T12:00:00Z"
}
```

### Redirect to Original URL
```http
GET /get-full-path?short_code=generated_short_code
```

This will redirect to the original URL.

## Development

### Code Quality

The project uses Ruff for linting and formatting. To run the linter:
```bash
task check
```

To format the code:
```bash
task format
```

### Database Migrations

To create a new migration:
```bash
task makemigrations -- "migration message"
```

To apply migrations:
```bash
task migrate
```

## Project Structure

```
url-shortener-py/
├── src/
│   ├── adapters/          # Adapters for web and storage
│   ├── application/       # Application use cases
│   ├── domain/           # Domain entities and rules
│   ├── infrastructure/   # Database and other infrastructure
│   └── main.py          # Application entry point
├── alembic/              # Database migrations
├── docker-compose.yaml   # Docker services configuration
├── pyproject.toml       # Project dependencies and configuration
└── README.md           # This file
```
