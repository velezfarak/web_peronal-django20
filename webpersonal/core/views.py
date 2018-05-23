from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    
    return render(request, "core/home.html")

def abaut(request):
    
    return render(request, 'core/abaut.html')

def contacto(request):
    
    return render(request,'core/contacto.html')