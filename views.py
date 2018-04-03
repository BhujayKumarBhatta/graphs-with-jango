# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render

# Create your views here.


def home(request):
    context = 'Hello Bhujay'
    return render(request,'home.html')
