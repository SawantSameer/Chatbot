from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("This is my first urls")

def specific(request):
    l = [1,2,5,4]
    return HttpResponse(l)

# Infact I can show anything to the url:
# like-- o numbers
#         o list...

def article(request, article_id):
    return render(request, "blog/index.html")

