from django.contrib import admin
from django.urls import path
from .views import cart,addtocart,checkout,confirmation
urlpatterns = [
    path('cart/',cart,name='cart'),
    path('addtocart/',addtocart,name='addtocart'),
    path('checkout/',checkout,name='checkout'),
    path('confirmation/',confirmation,name='confirmation')
]
