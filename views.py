# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render
# Create your views here.
def home(request):
    context = 'Hello Bhujay'
    return render(request,'home.html')

def home2(request):
    context = 'Hello Bhujay'
    return render(request,'home2.html')

def svg(request):
    ds1 = [10, 5, 10, 100, 15, 18, 25, 20, 18, 50, 70, 100,1,2,3, 10 , 15, 9, 7 , 40, 14, 55, 75, 80, 85, 100, 99, 95,
           10, 5, 10, 100, 15, 18, 25, 20, 18, 50, 70, 100,1,2,3, 10 , 15, 9, 7 , 40, 14, 55, 75, 80, 85, 100, 99, 95 ]
    #ds1 = [ 5, 10, 13, 19, 21, 25, 22, 18, 15, 13,
    #11, 12, 15, 20, 18, 17, 16, 18, 23, 25 ]
    context = {'ds1': ds1, 'msg': 'Hello Bhujay'}
    return render(request,'svg.html', context)

def svgline(request):
    ds1 = [10, 5, 10, 100, 15, 18, 25, 20, 18, 50, 70, 100,1,2,3, 10 , 15, 9, 7 , 40, 14, 55, 75, 80, 85, 100, 99, 95,
           10, 5, 10, 100, 15, 18, 25, 20, 18, 50, 70, 100,1,2,3, 10 , 15, 9, 7 , 40, 14, 55, 75, 80, 85, 100, 99, 95,
           55, 75, 80, 85, 100, 99, 95,55, 75, 80, 85, 100, 99, 95,55, 75, 80, 85, 100, 99, 95,55, 75, 80, 85, 100, 99, 95 ]
    #ds1 = [ 5, 10, 13, 19, 21, 25, 22, 18, 15, 13,
    #11, 12, 15, 20, 18, 17, 16, 18, 23, 25 ]
    context = {'ds1': ds1, 'msg': 'Hello Bhujay'}
    return render(request,'svgline.html', context)

def rickshaw1(request):    
    ds1 = [ 
            { x: 0, y: 40 }, 
            { x: 1, y: 49 }, 
            { x: 2, y: 38 }, 
            { x: 3, y: 30 }, 
            { x: 4, y: 32 } ]
    context = {'ds1': ds1, 'msg': 'Hello Bhujay'}
    return render(request,'rickshaw1.html', context)

