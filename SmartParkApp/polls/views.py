from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')

def privhome(requet):
    return render(requet, 'index.html')