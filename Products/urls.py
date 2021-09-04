from django.urls import path
from .views import home,getnavbar,category,product
urlpatterns=[
    path('',home,name='home'),
    path('category/',category,name='category'),
    path('getnavbar/',getnavbar,name='getnavbar'),
    path('product/<slug>/',product,name='product'),
    path('product/',product,name='product_url'),

]