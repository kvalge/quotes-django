from django.shortcuts import render
from django.http import HttpResponse
from quotes_app.models import Quote

def home(response):
    quotes = Quote.objects.all().order_by('author')
    return render(response, "home.html", {"quotes": quotes})
