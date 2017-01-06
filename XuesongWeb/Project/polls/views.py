from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'static/index.html', {'user': 'user'})


def about(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'static/about.html', {'user': 'user'})


def contacts(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'static/contacts.html', {'user': 'user'})


def connect4(request):
    return render(request, 'static/connect4.html', {'user': 'user'})
