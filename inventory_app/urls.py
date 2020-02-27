from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop),
    path('cart', views.cart),
    path('cart/update', views.update),
    path('checkout', views.checkout)
]