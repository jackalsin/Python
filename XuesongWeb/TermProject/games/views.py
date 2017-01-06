from django.shortcuts import render
from django.http import HttpResponse

import json

# Create your views here.
from games.models import Record


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def saveRecord(request):
    username = request.GET['username']
    score = request.GET['moves']
    newRecord = Record(username=username, score=int(float(score)))
    newRecord.save()
    return HttpResponse("Ok")


def scoreBoardHandler(request):
    allRecordsSet = Record.objects.all()
    recordArray = []
    for child in allRecordsSet:
        d = dict()
        d['username'] = child.username
        d['score'] = child.score
        recordArray.append(d)

    dumpRes = json.dumps(sorted(recordArray, key=lambda x: x['score']))
    return HttpResponse(dumpRes)
