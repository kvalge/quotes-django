from django.shortcuts import render
from django.http import HttpResponse
from quotes_app.models import Quote

def home(response):
    ls = Quote.objects.all()
    return render(response, "home.html", {"ls": ls})
