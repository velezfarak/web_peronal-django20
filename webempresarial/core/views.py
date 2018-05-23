from django.shortcuts import render,  HttpResponse

# Create your views here.

def home(request):

    
    return render(request, 'core/home.html')

def abaut(request):

    return render(request, 'core/about.html') 




def store(request):

    return render(request, 'core/store.html') 




def sample(request):

    return render(request, 'core/../pages/templates/pages/sample.html')
