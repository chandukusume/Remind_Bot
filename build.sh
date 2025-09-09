#!/bin/bash

echo "Building Docker images for Rasa chatbot..."

# Build all services
docker-compose build

echo "Starting all services..."
docker-compose up -d

echo "Services started:"
echo "- Rasa Server: http://localhost:5005"
echo "- Action Server: http://localhost:5055"
echo "- Telegram Bridge: http://localhost:5006"

echo "To view logs: docker-compose logs -f"
echo "To stop services: docker-compose down"