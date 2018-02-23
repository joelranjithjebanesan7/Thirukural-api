# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from thirukural.models import *

# Create your views here.
 
def kural_list(request):
    data = {}
    if "q" in request.GET:
        kural_list = Thirukural.objects.filter(Verse__contains=request.GET["q"])
        data["q"] = request.GET["q"]
    else:
        kural_list = Thirukural.objects.all()
    paginator = Paginator(kural_list, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        kurals = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        kurals = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        kurals = paginator.page(paginator.num_pages)
    
    data["kurals"] = kurals 

    return render(request, 'thirukural_list.html', data)