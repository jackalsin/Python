from django.shortcuts import render
from models import Drawing
from django.http import HttpResponse
# Create your views here.

def loadDrawingsRequest(request):
    drawings = Drawing.objects.all()
    result = ""
    for drawing in drawings:
        result = result + drawing.DrawingID+","
        result = result + drawing.BuildingName+","
        result = result + str(drawing.ConstructedYear)+","
        result = result + drawing.Contractor+","
        result = result + drawing.Floor+","
        result = result + drawing.Shop+";"

    return HttpResponse(result)

def addDrawingRecord(request):
    try:

        drawingID = request.GET["DrawingID"]
        BuildingName = request.GET["BuildingName"]
        ConstructedYear = request.GET["ConstructedYear"]
        Contractor = request.GET["Contractor"]
        Floor = request.GET["Floor"]
        Shop = request.GET["Shop"]

        newDrawing = Drawing(DrawingID = drawingID,BuildingName=BuildingName,ConstructedYear=ConstructedYear,Contractor=Contractor,Floor=Floor,Shop=Shop)
        newDrawing.save()
        return HttpResponse("OK")
    except:
        return HttpResponse("Failed")


def updateDrawingRecord(request):
    try:
        drawingID = request.GET["DrawingID"]
        BuildingName = request.GET["BuildingName"]
        ConstructedYear = request.GET["ConstructedYear"]
        Contractor = request.GET["Contractor"]
        Floor = request.GET["Floor"]
        Shop = request.GET["Shop"]

        drawingRecord = Drawing.objects.get(DrawingID=drawingID)

        drawingRecord.BuildingName = BuildingName
        drawingRecord.ConstructedYear = ConstructedYear
        drawingRecord.Contractor = Contractor
        drawingRecord.Floor = Floor
        drawingRecord.Shop= Shop

        drawingRecord.save()

        return HttpResponse("OK")
    except:
        return HttpResponse("Failed")

