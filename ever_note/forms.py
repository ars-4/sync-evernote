from django.forms import ModelForm
from django import forms

class CreateNoteForm(forms.Form):
    title = forms.CharField(max_length=244)
    description = forms.CharField(max_length=244)
