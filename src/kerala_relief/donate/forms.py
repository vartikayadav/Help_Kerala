from django import forms
from .models import Donate
class UserDonateForm(forms.ModelForm):

    class Meta:
        model=Donate
        fields=[
        'name',
        'email',
        'moblie_no',
        'amount',
        ]
