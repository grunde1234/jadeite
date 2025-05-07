from django import forms
from .models import Courses

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['coursename', 'coursecode', 'level', 'duration', 'fee']