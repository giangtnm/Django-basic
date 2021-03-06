# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Customer


# Create your views here.
def listing(request):
    customer_list = Customer.objects.all()
    paginator = Paginator(customer_list, 5)

    page_number = request.GET.get('page')
    try:
        customers = paginator.page(page_number)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)

    return render(request, 'list.html', {'customers': customers})
