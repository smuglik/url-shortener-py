FROM python:3.13-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

RUN groupadd -r app && useradd -r -g app app

WORKDIR /opt/url-shortener

COPY pyproject.toml uv.lock start.sh ./


RUN uv sync --no-dev --no-cache

COPY src/ ./src/
COPY alembic.ini ./

RUN mkdir -p /var/lib/url-shortener && \
    chown -R app:app /opt/url-shortener /var/lib/url-shortener

FROM python:3.13-slim AS runtime

COPY --from=builder /bin/uv /bin/uvx /bin/

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN groupadd -r app && useradd -r -g app app

WORKDIR /opt/url-shortener

COPY --from=builder --chown=app:app /opt/url-shortener ./
ENV PATH="/opt/url-shortener/.venv/bin/:${PATH}"
RUN chmod +x ./start.sh
USER app

CMD ["./start.sh"]
