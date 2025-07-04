# Use Python 3.10 slim base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system build tools required for packages like pandas
RUN apt-get update && apt-get install -y build-essential

# Copy all files into the container
COPY . .

# Upgrade pip and install all Python packages
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Expose the port used by Gunicorn
EXPOSE 5000

# Start the Flask app using Gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]