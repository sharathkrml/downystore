from django.shortcuts import render
from django.http import JsonResponse
from .models import Category,Product
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
    category=Category.objects.filter(slug=cat_slug).first()
    products=Product.objects.filter(category=category)
    return render(request,'Products/category.html',{'title':category,'products':products})

def product(request,slug):
    #http://127.0.0.1:8000/product/reebok-basketball-question-mid-shoes/
    for i in Product.objects.all():
        if(i.slug==slug):
            the_product=i
    return render(request,'Products/product.html',{'product':the_product,'title':the_product.name})

