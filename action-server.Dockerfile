# This is action-server.Dockerfile
FROM rasa/rasa-sdk:latest
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY actions /app/actions
#CMD ["run", "actions", "--cors", "*", "--port", "8080"]
# Add this command to list all files in the /app directory
CMD ["ls", "-R", "/app"]