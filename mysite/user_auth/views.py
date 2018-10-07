# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from .forms import RegisterForm
from django.shortcuts import render

# Create your views here.
def register(request):
    if request.method == 'POST':
        response = HttpResponse()
        response.write("<h1>Thanks for registering.</h1></br>")
        response.write("Your name: " + request.POST['username'] + "</br>")
        response.write("Your email: " + request.POST['email'] + "</br>")
        return response

    register_form = RegisterForm()
    return render(request, 'user_auth/register.html', {'form': register_form})
