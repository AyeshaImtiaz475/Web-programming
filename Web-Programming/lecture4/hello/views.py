from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    #return HttpResponse("Hello!")
    return render(request, "hello/index.html")

def ayesha(request):
    return HttpResponse("Hello, ayesha!. Just a reminder don't quit this until you are done")

def muqaddas(request):
    return HttpResponse("Hello, muqaddas! Welcome back to Django framework learning")

def poem(request):
    return HttpResponse("Twinkle, twinkle, little star, How I wonder what you are!  Up above the world so high,  like a diamond in the sky.  Twinkle, twinkle, little star,  How i wonder what you are?")

def greet(request, name):
    #return HttpResponse(f"Hello, {name.capitalize()}!")
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })