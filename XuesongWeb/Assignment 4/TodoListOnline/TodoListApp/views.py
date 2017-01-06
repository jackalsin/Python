from django.http import HttpResponse
from django.shortcuts import render
from models import Task
import json

# Create your views here.
def checkExistID(request):
    id = request.GET['TaskId']
    if Task.objects.filter(TaskId=id).count() > 0:
        return HttpResponse("true")
    else:
        return HttpResponse('false')


def addTask(request):
    # "/addTask?TaskId=" + idToAdd + "&desInput=" + descriptionInput
    # "&dueDateInput=" + dueDateInput + "&statusInput=" + statusInput
    taskId = request.GET['TaskId']
    descriptionInput = request.GET['desInput']
    dueDateInput = request.GET['dueDateInput']
    statusInput = request.GET['statusInput']
    if statusInput == 'on':
        statusInput = False
    else:
        statusInput = True

    # TaskId = models.CharField(max_length=8)
    # Description = models.CharField(max_length=30)
    # DueDate = models.DateField()
    # true means finished, false means unfinished.
    # Status = models.BooleanField()
    newTask = Task(TaskId=taskId, Description=descriptionInput, DueDate=dueDateInput, Status=statusInput)
    newTask.save()
    return HttpResponse("OK")


def loadTasks(request):
    tasksSet = Task.objects.all()
    taskArrayToReturn = []
    for task in tasksSet:
        d = dict()
        d["TaskID"] = task.TaskId
        d["Description"] = task.Description
        d["DueDate"] = str(task.DueDate)
        d["Status"] = task.Status
        taskArrayToReturn.append(d)
    dumpRes = json.dumps(taskArrayToReturn)
    print dumpRes
    return HttpResponse(dumpRes, content_type="text/plain")