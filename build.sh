#!/usr/bin/env bash
set -o errexit

# 1. Install & Prepare
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# 2. Secure Superuser (Uses Environment Variables from Render Dashboard)
# No more plain-text passwords here!
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
import os
User = get_user_model()
username = os.environ.get('SUPERUSER_USERNAME', 'devesh')
password = os.environ.get('SUPERUSER_PASSWORD')

if password and not User.objects.filter(username=username).exists():
    user = User.objects.create_superuser(username, 'devesh@srmcem.ac.in', password)
    user.is_approved = True
    user.save()
    print("Admin account verified.")
EOF

# 3. Keep this for Free Tier stability
python bulk_import.py