from django.shortcuts import redirect, render
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
            quote_req.save()
            messages.success(request, "New quote submitted!")
            return render(request, "new.html")
    else:
        quote_req = QuoteForm()
        context = {
        'quote_req':quote_req
    }
        return render(request, "new.html", context)


def edit(response):
    quotes = Quote.objects.all().order_by('author')
    return render(response, "edit.html", {"quotes": quotes})
    

""" def update(request, id):
    quote = Quote.objects.get(id=id)

    if(request.method == "POST"):
        form = QuoteForm(request.POST, instance=quote)
        if form.is_valid():
           form.save()
    else:
        form = QuoteForm
    return render(request, "edit.html") """

