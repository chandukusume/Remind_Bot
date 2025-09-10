#!/usr/bin/env python3
import subprocess
import sys

def train_model():
    """Train the Rasa model"""
    try:
        print("🚀 Training Rasa model...")
        result = subprocess.run(['rasa', 'train'], check=True, capture_output=True, text=True)
        print("✅ Model trained successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Training failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

if __name__ == "__main__":
    if train_model():
        sys.exit(0)
    else:
        sys.exit(1)