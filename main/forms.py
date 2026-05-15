from django import forms
from .models import Student, Course, Registration

class StudentForm(forms.ModelForm):
 class Meta:
    model = Student
    fields = '__all__'

#connects Student MODEL To user input
#handles validation automatically.

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['student', 'course', 'grade']