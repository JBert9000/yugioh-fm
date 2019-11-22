from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'main/home.html')

def guide(request):
    return render(request, 'main/guide.html')

def streams(request):
    return render(request, 'main/streams.html')
