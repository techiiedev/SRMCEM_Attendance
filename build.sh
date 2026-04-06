#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Install dependencies
echo "Installing requirements..."
pip install -r requirements.txt

# 2. Collect Static Files (CSS/Images)
echo "Collecting static files..."
python manage.py collectstatic --no-input

# 3. Run Database Migrations
echo "Running migrations..."
python manage.py migrate

# 4. Create Superuser (Admin) Automatically
# This uses a Python "here-doc" to run code inside the Django environment
echo "Creating Superuser..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
username = 'devesh'
email = 'devesh@srmcem.ac.in'
password = 'dev@123' 

if not User.objects.filter(username=username).exists():
    user = User.objects.create_superuser(username, email, password)
    user.is_approved = True  # Automatically approve the admin
    user.save()
    print(f"Superuser {username} created and approved.")
else:
    print(f"Superuser {username} already exists.")
EOF

# 5. Import Students and Subjects
# This runs your custom script to fill the database with SRMCEM data
echo "Importing Student and Subject data..."
if [ -f bulk_import.py ]; then
    python bulk_import.py
else
    print "bulk_import.py not found, skipping data import."
fi

echo "Build Process Completed Successfully!"