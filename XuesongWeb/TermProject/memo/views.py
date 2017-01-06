from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
import json

# Create your views here.
from memo.models import Memo


def addMemo(request):
    name = request.GET["name"]
    email = request.GET["email"]
    phone = request.GET["phone"]
    text = request.GET["text"]
    print (name, email, text, phone)
    memo = Memo()
    memo.Name = name
    memo.Email = email
    memo.Phone = phone
    memo.Text = text
    memo.save()
    return HttpResponse("Succeed")


def memo(request):
    if request.user.is_authenticated:
        return render(request, "allMemo.html")
    else:
        return redirect("/admin/")


def getMemo(request):
    if request.user.is_authenticated:
        rtnStr = json.dumps({"rtn": getMemoFromDatabase()})
        return HttpResponse(rtnStr)
    else:
        return redirect("/admin/")


'''
Return a json string format {"rtnList": []}
'''


def getMemoFromDatabase():
    rtnList = list()
    memos = Memo.objects.all()
    for memo in memos:
        child = dict()
        child["name"] = memo.Name
        child["text"] = memo.Text
        child["phone"] = memo.Phone
        child["email"] = memo.Email
        rtnList.append(child)
    return rtnList
