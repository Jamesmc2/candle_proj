from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop),
    path('cart', views.cart),
    path('cart/add', views.cart_add),
    path('cart/update', views.cart_update),
    path('checkout', views.checkout)
]