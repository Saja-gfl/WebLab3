# forms.py
from django import forms
from .models import Student, Address

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age']  # Add fields relevant to the Student model

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'city', 'postal_code']
