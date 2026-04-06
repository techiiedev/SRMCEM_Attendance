#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files (CSS/JS) into one folder for production
python manage.py collectstatic --no-input

# Apply any database changes
python manage.py migrate