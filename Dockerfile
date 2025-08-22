# Start from the official Rasa image
FROM rasa/rasa:latest-full

# Set the working directory inside the container
WORKDIR /app

# Copy all your project files into the container
COPY . /app

# This command will be run when the container starts
CMD ["run", "-m", "models", "--enable-api", "--cors", "*", "--port", "8080"]