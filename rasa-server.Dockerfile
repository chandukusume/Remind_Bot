# This Dockerfile builds the main Rasa server
FROM rasa/rasa:latest-full
WORKDIR /app
COPY . /app
CMD ["run", "--enable-api", "--cors", "*", "--port", "8080"]