from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.




def index(request):
    return render(request, "blog/index.html")

def specific(request):
    l = [1,2,5,4]
    return HttpResponse(l)

# Infact I can show anything to the url:
# like-- o numbers
#         o list...

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    return HttpResponse(userMessage)