from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# main screen: has messages, agents, users, and message box
@login_required
def dashboard(request):
    return HttpResponse('dashboard')

# client info screen
@login_required
def client(request):
    pass

# agent bio screen
@login_required
def bio(request):
    pass

# recipient page for sending the message
@login_required
def message(request):
    pass

# recipient page for updating bio
@login_required
def updBio(request):
    pass

# recipient page for updating data on clients
@login_required
def updData(request):
    pass
