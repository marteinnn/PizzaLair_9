from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/cart
    path('', views.cart, name="cart"),
]