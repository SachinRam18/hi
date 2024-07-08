# Use the official Python base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install netcat (nc)
RUN apt-get update && apt-get install -y netcat-traditional

# Install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files into the Docker image
COPY . /code/

# Copy .env file to the Docker image
COPY .env /code/.env

# Command to run when the container starts
CMD ["sh", "-c", "while ! nc -z db 5432; do sleep 1; done && python manage.py runserver 0.0.0.0:8000"]
