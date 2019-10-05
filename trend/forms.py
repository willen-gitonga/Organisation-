from django import forms
from .models import Bursary
from django.contrib.auth.models import User

class BursaryForm(forms.ModelForm):
    class Meta:
        model = Bursary
        exclude = ['user']
