from django.shortcuts import render
from django.contrib import messages
from .forms import QuoteForm
from quotes_app.models import Quote

def home(response):
    quotes = Quote.objects.all().order_by('author')
    return render(response, "home.html", {"quotes": quotes})


def new(request):
    if request.method == "POST":
        quote_req = QuoteForm(request.POST)
        if quote_req.is_valid():
            author = quote_req.cleaned_data["author"]
            quote = quote_req.cleaned_data["quote"]
            years = quote_req.cleaned_data["years"]
            area = quote_req.cleaned_data["area"]
            image = quote_req.cleaned_data["image"]

            Quote.objects.create(author=author,
                                quote=quote,
                                years=years,
                                area=area,
                                image=image)
            messages.success(request, "New quote submitted!")
    return render(request, "new.html")
