from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("carrinho.html", views.carrinho, name='carrinho'),
    path("produtos.html", views.produtos, name= 'produto'),
    path("questions", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

