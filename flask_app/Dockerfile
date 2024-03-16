# Use the official Python image as a base image
FROM python

# Set the working directory inside the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install Flask and requests dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the Flask application code into the container
COPY . .

# Expose port 8000
EXPOSE 8000

# Command to run the Flask application
CMD ["python3", "app.py"]

