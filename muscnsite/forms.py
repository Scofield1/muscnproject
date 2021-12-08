from django import forms
from .models import Contact, Subscribers

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ['name', 'email',]
