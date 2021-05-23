from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')

def planos(request):
    return render(request, 'planos.html')

def login(request):
    return render(request, 'login.html')

def privhome(requet):
    return render(requet, 'index.html')
