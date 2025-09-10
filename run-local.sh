#!/bin/bash

echo "🚀 Starting Rasa bot locally..."

# Train model first
echo "📚 Training model..."
python train.py

if [ $? -ne 0 ]; then
    echo "❌ Training failed. Exiting."
    exit 1
fi

# Start action server in background
echo "🔧 Starting action server..."
rasa run actions --debug &
ACTION_PID=$!

# Wait for action server to start
sleep 5

# Start Rasa server in background
echo "🤖 Starting Rasa server..."
rasa run --enable-api --cors "*" --debug &
RASA_PID=$!

# Wait for Rasa server to start
sleep 10

# Start telegram bridge
echo "📱 Starting Telegram bridge..."
python telegram_bridge.py &
TELEGRAM_PID=$!

echo "✅ All services started!"
echo "- Action Server: http://localhost:5055"
echo "- Rasa Server: http://localhost:5005"
echo "- Telegram Bridge: http://localhost:5006"

# Function to cleanup on exit
cleanup() {
    echo "🛑 Stopping services..."
    kill $ACTION_PID $RASA_PID $TELEGRAM_PID 2>/dev/null
    exit 0
}

# Set trap to cleanup on script exit
trap cleanup SIGINT SIGTERM

# Wait for user to stop
echo "Press Ctrl+C to stop all services"
wait