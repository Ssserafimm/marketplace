FROM python:3.10-slim
RUN apt-get update && apt-get install -y netcat-openbsd gcc
WORKDIR /app
COPY . .
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8003"]