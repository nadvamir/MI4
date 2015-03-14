from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from models import *

# main screen: has messages, agents, users, and message box
@login_required
@csrf_protect
def dashboard(request):
    # a list of messages
    messages = [{
        'sender': m.fromName,
        'recipient': m.toName,
        'content': m.message
        } for m in Message.get(request.user.id)]

    # a list of users
    users = [{
        'id': u.id,
        'username': u.username
        } for u in Agent.list()]

    # a list of clients
    clients = [{
        'id': c.matr,
        'name': c.name
        } for c in Client.list()]

    context = RequestContext(request)
    context_dict = {
        'user': request.user,
        'messages': messages,
        'users': users,
        'clients': clients,
    }

    return render_to_response('dashboard.html', context_dict, context)

# client info screen
@login_required
def client(request, client_id):
    return HttpResponse('client')

# agent bio screen
@login_required
def bio(request, agent_id):
    return HttpResponse('bio')

# recipient page for sending the message
@login_required
def message(request, agent_id):
    return HttpResponse('message')

# recipient page for updating bio
@login_required
def updBio(request, agent_id):
    return HttpResponse('upd bio')

# recipient page for updating data on clients
@login_required
def updData(request, client_id):
    return HttpResponse('upd data')
