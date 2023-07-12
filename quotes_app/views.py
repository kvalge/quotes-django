from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .forms import QuoteForm
from quotes_app.models import Quote
from django.views.decorators.csrf import csrf_protect


def home(response):
    quotes = Quote.objects.all().order_by('author')
    return render(response, "home.html", {"quotes": quotes})


@csrf_protect
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
    
    
@csrf_protect
def update(request,id):
    try:
        old_data = get_object_or_404(Quote,id =id)
    except Exception:
        raise Http404('Does Not Exist')
    if request.method =='POST':
        form =QuoteForm(request.POST, instance =old_data)
 
        if form.is_valid():
            form.save()
            return redirect('/edit')
    else:
        form = QuoteForm(instance = old_data)
        context ={
            'form':form
        }
        return render(request,'update.html',context)
    return render(request, 'update.html', {'form': form})


@csrf_protect
def delete(request, id):
    try:
        data = get_object_or_404(Quote,id = id)
    except Exception:
        raise Http404('Does Not Exist')
 
    if request.method == 'POST':
        data.delete()
        return redirect('/edit')
    else:
        return render(request, 'delete.html')

