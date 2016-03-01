__author__ = 'thomas'

from django.http import Http404, HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
import datetime


def hello(request):
    return HttpResponse("hello,world")

def showdate(request):
    now = datetime.datetime.now()
    # t = get_template('current_datetime.html')
    # html = t.render(Context({'current_date':now}))
    # return HttpResponse(html)
    return render_to_response('current_datetime.html',{'current_date':now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def display_meta(request):
    values = sorted(request.META.items())
    return render_to_response('display.html',{'values':values})