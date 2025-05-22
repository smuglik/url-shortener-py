#!/bin/sh

alembic upgrade heads &&
  granian --interface asgi --workers 4 --host 0.0.0.0 --port 8000 src/main:app
