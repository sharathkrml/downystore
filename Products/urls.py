from django.urls import path
from .views import home,getnavbar
urlpatterns=[
    path('',home,name='home'),
    path('getnavbar/',getnavbar,name='getnavbar')
]