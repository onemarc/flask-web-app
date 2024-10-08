# Use the official Python image from the Docker Hub
FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENV NAME World

CMD ["gunicorn", "-b", ":8080", "app.main:app"]