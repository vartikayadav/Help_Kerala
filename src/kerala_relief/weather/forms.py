from django import forms
from .models import City

class CityForm(forms.ModelForm):
    name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={
    'placeholder':"City name"
    }))
    class Meta:
        model=City
        fields=[
        'name'
        ]
