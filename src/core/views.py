from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def cadastro(resquest):
    return render(request, 'cadastro.html')
