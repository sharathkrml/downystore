from django.urls import path
from .views import myorders,logout_view,login_view, profile,signup_view,forgot,cards,cards_edit,verify,reset,address_edit,profile,address
urlpatterns=[
    path('logout/',logout_view,name='logout'),
    path('login/',login_view,name='login'),
    path('signup/',signup_view,name='signup'),
    path('forgot/',forgot,name='forgot'),
    path('verify/',verify,name='verify'),
    path('reset/',reset,name='reset'),
    path('profile/',profile,name='profile'),
    path('profile/address/',address,name='address'),
    path('profile/cards/',cards,name='cards'),
    path('profile/address/edit/',address_edit,name='address_edit'),
    path('profile/cards/edit/',cards_edit,name='cards_edit'),
    path('myorders/',myorders,name='myorders')
]