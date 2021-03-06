from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
    path('delete', views.delete),
    path('edit_account', views.edit_account),
    path('user_page', views.user_page),
    path('favorite_list/<int:scent_id>', views.add_favorite),
]