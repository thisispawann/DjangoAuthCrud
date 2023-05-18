from django import forms
from crud.models import Student

class StudentForm(forms.Form):
    class Meta:
        model = Student
        fields = '__all__'