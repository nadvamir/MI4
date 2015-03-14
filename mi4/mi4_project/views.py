from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    return HttpResponse('text')

# main screen: has messages, agents, users, and message box
def dashboard(request):
    pass

# client info screen
def client(request):
    pass

# agent bio screen
def bio(request):
    pass

# recipient page for sending the message
def message(request):
    pass

# recipient page for updating bio
def updBio(request):
    pass

# recipient page for updating data on clients
def updData(request):
    pass
