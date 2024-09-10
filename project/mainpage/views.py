from django.shortcuts import render

def index(request): 
    return render( 
        request,     # так будет всегда(первым параметром будет request) 
        'mainpage/index.html', 
        context={ 
        } 
    )# Create your views here.
