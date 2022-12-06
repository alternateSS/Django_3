from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Client, Account, Credit
from django.views import generic


class ClientView(generic.ListView):
    model = Client
    template_name = 'clients.html'
    context_object_name = 'clients_list'

