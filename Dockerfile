# Dockerfile for backend
FROM python:3.10-slim

WORKDIR /app

COPY safety_report_trial/backend/ ./backend/
COPY safety_report_trial/requirements.txt ./requirements.txt

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
