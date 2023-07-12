from django import forms
from django.forms import ModelForm
from .models import Quote

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['author', 'quote', 'years', 'area', 'image']