# Use the official Python image for Windows
FROM python:3-alpine3.15

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port that the app will run on
EXPOSE 5000

# Command to run the application
CMD ["python", "main.py"]
