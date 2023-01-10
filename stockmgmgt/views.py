from django.shortcuts import render, redirect
from .models import Stock
from .forms import stockCreateForm

# Create your views here.

def home(request):
  title = 'voorraad - koelkast'
  context = { 
  "title": title,
  }
  
  return render(request, "home.html", context)

def list_items(request):
  title = 'List of items'
  queryset = Stock.objects.all()
  context = { "title": title,
              "queryset": queryset,
  }
  
  return render(request, "list_items.html", context)

def add_items(request):
  form = stockCreateForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('/list_items')
  context = {
    "form": form,
    "title": "Add Item",
  }

  return render(request, "add_items.html", context)