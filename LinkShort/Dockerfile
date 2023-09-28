ARG PYTHON_VERSION=3.10-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY "npKkkNeqzrwSbF63HXwfSJM8dJY02M0uxuIVeXeMXCGLqe1JzG"
ENV DATABASE_URL "postgres://postgres:HmqGhw1NfrYpKxs@ianv-db.internal:5432/ianv"

# install psycopg2 dependencies.
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/
COPY . /code

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "LinkShort.wsgi"]
