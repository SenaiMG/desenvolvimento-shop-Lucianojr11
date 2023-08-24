from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def carrinho(request):
    return render(request, 'carrinho.html')

def produtos(request):
    return render(request, 'produtos.html')

def detail(request, question_id):
    return HttpResponse("Você esta procurando" % question_id)

def results(request, question_id):
    response = "Você encontrou os resultados das perguntas %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Você votou nas perguntas %s." % question_id)

