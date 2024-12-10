from django.contrib import admin
from .models import Author, Genre, Book
from .models import Address, Student

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'city')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'address')

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
