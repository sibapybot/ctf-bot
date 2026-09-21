FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml ./
COPY README.md ./
COPY uv.lock ./
COPY main.py ./
COPY src ./src

RUN pip install --no-cache-dir uv && uv pip install --system --no-cache .

CMD ["python", "main.py"]
