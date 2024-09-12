from django.shortcuts import render

def index(request): 
    return render( 
        request,     # так будет всегда(первым параметром будет request) 
        'mainpage/index.html', 
        context={ 
        } 
    )# Create your views here.

def contacts(request): 
    return render( 
        request,     # так будет всегда(первым параметром будет request) 
        'mainpage/contacts.html', 
        context={ 
        } 
    )# Create your views here.
    
def about_us(request): 
    return render( 
        request,     # так будет всегда(первым параметром будет request) 
        'mainpage/about_us.html', 
        context={ 
        } 
    )# Create your views here.
    
def menu(request): 
    return render( 
        request,     # так будет всегда(первым параметром будет request) 
        'mainpage/menu.html', 
        context={ 
        } 
    )# Create your views here.
    
def services(request): 
    return render( 
        request,     # так будет всегда(первым параметром будет request) 
        'mainpage/services.html', 
        context={ 
        } 
    )# Create your views here.
    
    
    
