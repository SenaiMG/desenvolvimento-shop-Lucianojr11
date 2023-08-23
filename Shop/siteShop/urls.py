from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("carrinho.html", views.carrinho, name='carrinho'),
    path("produtos.html", views.produtos, name= 'produto'),
]