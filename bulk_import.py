import os
import csv
import django

# 1. Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from attendance.models import Student

def import_students(file_path):
    if not os.path.exists(file_path):
        print(f"❌ Error: File '{file_path}' not found.")
        return

    with open(file_path, mode='r', encoding='utf-8-sig') as file:
        # DictReader uses the first row as keys
        reader = csv.DictReader(file)
        
        # Clean whitespace from headers
        reader.fieldnames = [name.strip() for name in reader.fieldnames]
        
        count = 0
        duplicates = 0

        print("🚀 Starting Import...")

        for row in reader:
            # Mapping based on your CSV headers
            # Note: We skip 'Roll Number(username)' as per your core requirements
            u_roll = row.get('University Roll Number', '').strip()
            f_name = row.get('First Name', '').strip()
            l_name = row.get('Last Name', '').strip()
            email = row.get('Email Address', '').strip()
            s_class = row.get('Class', '').strip()

            if not u_roll:
                continue

            # Create or Update based on University Roll Number
            student, created = Student.objects.update_or_create(
                university_roll=u_roll,
                defaults={
                    'first_name': f_name,
                    'last_name': l_name,
                    'email': email,
                    'student_class': s_class
                }
            )

            if created:
                print(f"✅ Imported: {u_roll} - {f_name}")
                count += 1
            else:
                print(f"⚡ Updated: {u_roll}")
                duplicates += 1

    print(f"\n✨ Done! {count} students added, {duplicates} updated.")

if __name__ == "__main__":
    # Ensure this filename matches your actual file
    import_students('BCA_2024_STUDENT_LIST.csv')