from dataclasses import field
from django import forms
from .models import *


class Logreg(forms.ModelForm):
    class Meta:
        model = log
        fields = ['username', 'f_name', 'l_name', 'age', 'email', 'password', 'confirm', 'gender']

class user(forms.ModelForm):
    class Meta:
        model = log
        fields = ['id', 'username']

class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Email', required=True)
    subject = forms.CharField(label='About', required=True)
    message = forms.CharField(label='Message', widget=forms.Textarea, required=True)