"""
Website views
"""
from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting

def welcome(request):
    """Render welcome page, which includes number of meetings currently scheduled"""
    return render(
        request,
        'website/welcome.html',
        {"meetings": Meeting.objects.all()}
    )

def about(request):
    """Render the about page"""
    return HttpResponse("The author of this site is named Blake Sager")
