from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django import forms
from models import *
import re
import bleach

# main screen: has messages, agents, users, and message box
@login_required
@csrf_protect
def dashboard(request):
    if 'POST' == request.method:
        # insert a message
        toId = re.sub('/[^0-9]/', '', request.POST['toId'])
        msg = bleach.clean(request.POST['msg'])[:160]
        if None != Agent.get(toId):
            Message((None, request.user.id, toId, msg)).save()

    # display the dashboard as always
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
    client = Client.get(client_id)
    if None == client:
        return HttpResponseNotFound()

    if 'POST' == request.method:
        # update client data
        client = Client((
                client_id,
                bleach.clean(request.POST['name'])[:255],
                bleach.clean(request.POST['surname'])[:255],
                bleach.clean(request.POST['DOB'])[:255],
                bleach.clean(request.POST['email'])[:255],
                bleach.clean(request.POST['contactPhone'])[:255],
                bleach.clean(request.POST['role'])[:255],
                bleach.clean(request.POST['undercoverName'])[:255],
                bleach.clean(request.POST['undercoverSurname'])[:255],
                bleach.clean(request.POST['passphrase'])[:255]))
        client.save()

    # show the data for edditing
    context = RequestContext(request)

    return render_to_response('client.html', client.toDict(), context)

# agent bio screen
@login_required
def bio(request, agent_id):
    return HttpResponse('bio')

# recipient page for updating bio
@login_required
def updBio(request, agent_id):
    return HttpResponse('upd bio')

# recipient page for updating data on clients
@login_required
def updData(request, client_id):
    return HttpResponse('upd data')
