from django.http import HttpResponse
from django.shortcuts import render
from drawingSearchApp.search import DrawingSearch


# Create your views here.

def searchDrawing(request):

    text = request.GET["query"]
    print(text)
    response = DrawingSearch(text)
    if response == "Fail":
        return HttpResponse(response)
    else:
        return HttpResponse(response)

