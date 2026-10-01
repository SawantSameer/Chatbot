from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('chatbot', read_only = False, logic_adapters=['chatterbot.logic.BestMatch'])      #I can even create a bot to answer any mathematical questions, or of any specific task

list_to_train = [
    "hi",
    "Hi, there",
    "What is your name?",
    "My name is Jarvis",
    "My name is Sameer",
    "So what?"
]

list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)




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
    chatResponse = bot.get_response(userMessage)
    return HttpResponse(chatResponse)