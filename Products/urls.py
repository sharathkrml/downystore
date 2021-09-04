from django.urls import path
from .views import home,getnavbar,category
urlpatterns=[
    path('',home,name='home'),
    path('category/',category,name='category'),
    path('getnavbar/',getnavbar,name='getnavbar')
]