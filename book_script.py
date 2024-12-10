from bookmodule.models import Address, Book, Student


from bookmodule.models import Book

student = Student(name="John Doe", age=20)
student.save()
address = Address(student=student, street="123 Elm St", city="Springfield", postal_code="12345")
address.save()