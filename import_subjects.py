import os
import django

# 1. Setup Django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from attendance.models import Subject

def run_import():
    # 2. Define your SRMCEM Subjects
    subjects_list = [
        {'code': 'NBCA-301', 'name': 'Advance Java'},
        {'code': 'NBCA-302', 'name': 'Design and Analysis of Algorithm(DAA)'},
        {'code': 'NBCA-303', 'name': 'Web Design'},
        {'code': 'NBCA-304', 'name': 'Computer Graphics'},
        {'code': 'NBCA-305', 'name': 'Managerial Economics'},
    ]

    print("--- Starting SRMCEM Subject Sync ---")
    
    count = 0
    for sub in subjects_list:
        # get_or_create ensures we don't get errors if the subject exists
        obj, created = Subject.objects.get_or_create(
            code=sub['code'],
            defaults={'name': sub['name']}
        )
        if created:
            print(f"✅ Added: {sub['code']} - {sub['name']}")
            count += 1
        else:
            print(f"ℹ️ Verified: {sub['code']} exists.")

    print(f"--- Finished! Added {count} new subjects. ---")

if __name__ == "__main__":
    run_import()