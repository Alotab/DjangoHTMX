from django import forms
from .models import Person




class UpdatePerson(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'description']

