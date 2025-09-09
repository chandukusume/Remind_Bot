#!/bin/bash

# Azure deployment script for Rasa chatbot

echo "🚀 Starting Azure deployment for Rasa chatbot..."

# Check if required files exist
if [ ! -f "credentials.json" ]; then
    echo "❌ Error: credentials.json not found. Please add your Google Service Account credentials."
    exit 1
fi

if [ ! -f ".env" ]; then
    echo "❌ Error: .env file not found. Please create it from .env.example"
    exit 1
fi

# Load environment variables
source .env

echo "✅ Environment variables loaded"

# Build and deploy with docker-compose
echo "🔨 Building Docker images..."
docker-compose -f azure-compose.yml build

echo "🚀 Starting services..."
docker-compose -f azure-compose.yml up -d

echo "✅ Deployment complete!"
echo ""
echo "📊 Service Status:"
docker-compose -f azure-compose.yml ps

echo ""
echo "🌐 Your services are running on:"
echo "- Rasa Server: http://your-azure-vm-ip:80"
echo "- Action Server: http://your-azure-vm-ip:5055"
echo "- Telegram Bridge: http://your-azure-vm-ip:5006"
echo ""
echo "📝 To check logs: docker-compose -f azure-compose.yml logs -f"
echo "🛑 To stop services: docker-compose -f azure-compose.yml down"