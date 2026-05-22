#!/bin/bash
echo "Running tests..."
python -m pytest tests/
echo "Deploying..."
git push origin main
