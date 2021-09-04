from django.shortcuts import render
from django.http import JsonResponse
from .models import Category
# Create your views here.
def home(request):
    return render(request,'Products/home.html')

def getnavbar(request):
    meat_dict={
        'POULTRY':'?cat=poultry',
        'MUTTON':'?cat=mutton',
        'PORK':'?cat=pork',
    }
    seafood_dict={
        'CANNED SEAFOOD':'?cat=canned-seafood',
        'FRESH FISH':'?cat=fresh-fish',
        'SEA FOOD':'?cat=seafood',
        'PRAWN':'?cat=prawn'
    }
    return JsonResponse({'meat_dict':meat_dict,'seafood_dict':seafood_dict})

def category(request):
    cat_slug=request.GET.get('cat')
    print(cat_slug)
    return render(request,'Products/category.html')