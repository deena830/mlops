# Use an official Python runtime as a parent image
FROM python:latest

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /back/inback

# Copy the current directory contents into the container at /app
COPY . /back/inback
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the command to run your application
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
