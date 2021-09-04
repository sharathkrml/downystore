from django.shortcuts import render
from django.http import JsonResponse
from .models import Category
# Create your views here.
def home(request):
    return render(request,'Products/home.html')

def getnavbar(request):
    meat_dict={
        'POULTRY':'?category=poultry',
        'MUTTON':'?category=mutton',
        'PORK':'?category=pork',
    }
    seafood_dict={
        'CANNED SEAFOOD':'?category=canned-seafood',
        'FRESH FISH':'?category=fresh-fish',
        'SEA FOOD':'?category=seafood',
        'PRAWN':'?category=prawn'
    }
    return JsonResponse({'meat_dict':meat_dict,'seafood_dict':seafood_dict})
