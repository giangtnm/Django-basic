# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.http import HttpResponse
from django.shortcuts import render

from .forms import UploadFileForm


# Create your views here.
def file_uploader_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload(request.FILES['file'])
            return HttpResponse("<h2>File uploaded successful!</h2>")
        else:
            return HttpResponse("<h2>File uploaded unsuccessful!</h2>")

    form = UploadFileForm()
    return render(request, 'fileUploaderTemplate.html', {'form': form})


def upload(f):
    file = open(f.name, 'wb+')
    for chunk in f.chunks():
        file.write(chunk)
