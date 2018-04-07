# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render
import datetime , time
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
            { 'x': 0, 'y': 0 }, 
            { 'x': 5, 'y': 20 }, 
            { 'x': 10, 'y': 38 }, 
            { 'x': 15, 'y': 30 }, 
            { 'x': 20, 'y': 56 } ]
    
    gd = [(datetime.datetime(2018, 3, 19, 9, 25), 300.0, 0.211498618533826), 
           (datetime.datetime(2018, 3, 19, 9, 35), 300.0, 0.51186000010320402), 
           (datetime.datetime(2018, 3, 19, 9, 45), 300.0, 2), 
           (datetime.datetime(2018, 3, 19, 9, 55), 300.0, 14), 
           (datetime.datetime(2018, 3, 19, 10, 5), 300.0, 30), 
           (datetime.datetime(2018, 3, 19, 10, 15), 300.0, 40), 
           (datetime.datetime(2018, 3, 19, 10, 25), 300.0, 50),
           (datetime.datetime(2018, 3, 19, 10, 30), 300.0, 55), 
           (datetime.datetime(2018, 3, 19, 10, 35), 300.0, 70), 
           (datetime.datetime(2018, 3, 19, 10, 40), 300.0, 40), 
           (datetime.datetime(2018, 3, 19, 10, 45), 300.0, 45), 
           (datetime.datetime(2018, 3, 19, 10, 55), 300.0, 80),
           (datetime.datetime(2018, 3, 19, 11, 00), 300.0, 82), 
           (datetime.datetime(2018, 3, 19, 11, 05), 300.0, 85), 
           (datetime.datetime(2018, 3, 19, 11, 10), 300.0, 90), 
           (datetime.datetime(2018, 3, 19, 11, 15), 300.0, 100), 
           (datetime.datetime(2018, 3, 19, 11, 20), 300.0, 100),
           (datetime.datetime(2018, 3, 19, 11, 25), 300.0, 124),
           (datetime.datetime(2018, 3, 19, 11, 30), 300.0, 130), 
           (datetime.datetime(2018, 3, 19, 11, 35), 300.0, 140),
           ]
    ds2 = []
    for i in gd:
        a,b,c = i
        dict = {'x': int(time.mktime(a.timetuple())), 'y': c}
        ds2.append(dict)   
    
    context = {'ds1': ds1, 'ds2': ds2, 'msg': 'Hello Bhujay'}
    return render(request,'rickshaw1.html', context)

 
           
            
#            (datetime.datetime(2018, 3, 19, 11, 40), 300.0, 50),
#            (datetime.datetime(2018, 3, 19, 11, 45), 300.0, 55), 
#            (datetime.datetime(2018, 3, 19, 11, 50), 300.0, 70), 
#            (datetime.datetime(2018, 3, 19, 11, 55), 300.0, 40), 
#            (datetime.datetime(2018, 3, 19, 12, 00, 300.0, 45), 
#            (datetime.datetime(2018, 3, 19, 13, 05), 300.0, 80),
#            (datetime.datetime(2018, 3, 19, 13, 10), 300.0, 82), 
#            (datetime.datetime(2018, 3, 19, 13, 15), 300.0, 85), 
#            (datetime.datetime(2018, 3, 19, 13, 20), 300.0, 90), 
#            (datetime.datetime(2018, 3, 19, 13, 25), 300.0, 100), 
#            (datetime.datetime(2018, 3, 19, 13, 30), 300.0, 100))


#ds2 = [(datetime.datetime(2018, 3, 19, 9, 25, tzinfo=<FixedOffset u'+00:00' datetime.timedelta(0)>), 300.0, 0.211498618533826), (datetime.datetime(2018, 3, 19, 9, 35, tzinfo=<FixedOffset u'+00:00' datetime.timedelta(0)>), 300.0, 0.21186000010320402), (datetime.datetime(2018, 3, 19, 9, 45, tzinfo=<FixedOffset u'+00:00' datetime.timedelta(0)>), 300.0, 0.21243252666576), (datetime.datetime(2018, 3, 19, 9, 55, tzinfo=<FixedOffset u'+00:00' datetime.timedelta(0)>), 300.0, 0.211657972857297), (datetime.datetime(2018, 3, 19, 10, 5, tzinfo=<FixedOffset u'+00:00' datetime.timedelta(0)>), 300.0, 0.211205720023904), (datetime.datetime(2018, 3, 19, 10, 15, tzinfo=<FixedOffset u'+00:00' datetime.timedelta(0)>), 300.0, 0.211523038609912), (datetime.datetime(2018, 3, 19, 10, 25, tzinfo=<FixedOffset u'+00:00' datetime.timedelta(0)>), 300.0, 0.21524190015871103)]
#     gd = [(datetime.datetime(2018, 3, 19, 9, 25), 300.0, 0.211498618533826), 
#            (datetime.datetime(2018, 3, 19, 9, 35), 300.0, 0.51186000010320402), 
#            (datetime.datetime(2018, 3, 19, 9, 45), 300.0, 2), 
#            (datetime.datetime(2018, 3, 19, 9, 55), 300.0, 14), 
#            (datetime.datetime(2018, 3, 19, 10, 5), 300.0, 30), 
#            (datetime.datetime(2018, 3, 19, 10, 15), 300.0, 40), 
#            (datetime.datetime(2018, 3, 19, 10, 25), 300.0, 50),
#            (datetime.datetime(2018, 3, 19, 10, 30), 300.0, 55), 
#            (datetime.datetime(2018, 3, 19, 10, 35), 300.0, 70), 
#            (datetime.datetime(2018, 3, 19, 10, 40), 300.0, 40), 
#            (datetime.datetime(2018, 3, 19, 10, 45), 300.0, 45), 
#            (datetime.datetime(2018, 3, 19, 10, 55), 300.0, 80),
#            (datetime.datetime(2018, 3, 19, 11, 00), 300.0, 82), 
#            (datetime.datetime(2018, 3, 19, 11, 05), 300.0, 85), 
#            (datetime.datetime(2018, 3, 19, 11, 10), 300.0, 90), 
#            (datetime.datetime(2018, 3, 19, 11, 15), 300.0, 100), 
#            (datetime.datetime(2018, 3, 19, 10, 20), 300.0, 100)
#            ]

