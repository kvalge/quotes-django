from django import forms

class QuoteForm(forms.Form):
    author = forms.CharField(max_length=250)
    quote = forms.CharField(max_length=4500)
    years = forms.CharField(max_length=250)
    area = forms.CharField(max_length=150)
    image = forms.CharField(max_length=5000)