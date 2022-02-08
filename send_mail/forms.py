from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """Form of subscription at email"""
    class Meta:
        model = Contact
        fields = '__all__'
