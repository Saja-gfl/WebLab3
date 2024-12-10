import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')  # Replace `your_project_name` with your Django project name
django.setup()

# Import your models
from book.models import Address, Student # type: ignore

# Script logic
def populate_data():
    city1 = Address.objects.create(city='New York')
    city2 = Address.objects.create(city='Los Angeles')

    student1 = Student.objects.create(name='Alice', age=20, address=city1)
    student2 = Student.objects.create(name='Bob', age=22, address=city2)

    print("Data populated successfully!")

if __name__ == "__main__":
    populate_data()
