from django import forms
from .models import Student

class studentForm(forms.ModelForm):
    class Meta:
        model =Student
        fields= ["first_name", "last_name", "date_of_birth"]