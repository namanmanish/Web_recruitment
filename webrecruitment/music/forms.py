from django import forms
from .models import Person, City, College, State


class PersonForm(forms.ModelForm):
  class Meta:
   model = Person
   fields = ['name', 'state', 'city', 'college', 'age']
  

