#!/bin/bash

echo "🚀 Complete Rasa Bot Setup"

# Check if credentials.json exists
if [ ! -f "credentials.json" ]; then
    echo "❌ Please add your Google Service Account credentials.json file"
    echo "📝 Edit the placeholder credentials.json with your actual values"
    exit 1
fi

# Check if .env exists and has values
if [ ! -f ".env" ]; then
    echo "❌ .env file not found"
    exit 1
fi

# Make scripts executable
chmod +x *.sh

echo "✅ Setup complete!"
echo ""
echo "🔧 Available commands:"
echo "  ./run-local.sh          - Run bot locally for testing"
echo "  ./deploy-azure.sh       - Deploy to Azure with docker-compose"
echo "  ./azure-student-deploy.sh - Create Azure VM (student account)"
echo ""
echo "📋 Before deployment:"
echo "1. Update credentials.json with your Google Service Account"
echo "2. Verify .env file has correct values"
echo "3. Test locally first: ./run-local.sh"