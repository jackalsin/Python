# coding=utf-8
from __future__ import print_function
from django.conf import settings
import json

if not settings.configured:
    settings.configure()

from drawingManageApp.models import Drawing
from django.db.models import Q

import re


def DrawingSearch(keywords):
    """
    :param keywords:    keywords to search for the drawing information
                        example: “attributeValue1,attributeName1:attributeValue2,attributeName2:[valueLowerBo
                                undary-valueUpperBoundary], …”
    :return:
    """
    keywordDict = dict()
    RETURN_STR_ONLY_VAL = "The keyword #{0} only has a value {1}"
    RETURN_STR_KEY_VAL = "The keywod #{0} uses attribute name {1}, and has a value {2}"
    RETURN_STR_MUL_VAL = "The keyword #{0} uses attribute name {1}, and has a ranged value with lower \
boundary {2} and upper boundary {3}"
    IS_RANGE = True
    index = 1
    keywords = re.compile(r"[,]").split(keywords)
    for keyword in keywords:
        keywordPair = re.compile(r":").split(keyword)
        if len(keywordPair) == 2:  # has attribute print
            attriName = keywordPair[0]
            attriVal = keywordPair[1]
            if not attriVal.startswith("["):
                print(RETURN_STR_KEY_VAL.format(index, attriName, attriVal))
                keywordDict[attriName] = (not IS_RANGE, attriVal)
        else:  # only has value, no name
            attriName = None
            attriVal = keywordPair[0]
            if not attriVal.startswith("["):
                print(RETURN_STR_ONLY_VAL.format(index, attriVal))
                if "None" not in keywordDict:
                    keywordDict["None"] = list()
                keywordDict["None"].append((not IS_RANGE, attriVal))
        if re.compile(r"\[.+-.+\]").match(attriVal):
            attriValList = list()
            attriVals = attriVal.split("-")
            attriValList.append(attriVals[0].lstrip("["))
            attriValList.append(attriVals[1].rstrip("]"))
            print(RETURN_STR_MUL_VAL.format(index, attriName, attriValList[0], attriValList[1]))
            keywordDict[attriName] = (IS_RANGE, attriValList)
        index += 1
    print(keywordDict)
    QuerySet = Drawing.objects.all()
    ResultSet = QuerySet

    for key in keywordDict:
        if key == "DrawingID":
            value = keywordDict[key]
            if value[0]:  # is a Range
                ResultSet = ResultSet.filter(DrawingID__range=(value[1][0], value[1][1]))
            else:
                ResultSet = ResultSet.filter(DrawingID__exact=value[1])
        elif key == "BuildingName":
            # only Non range value BuildingNmae
            value = keywordDict[key]
            if value[0]:  # is a Range
                ResultSet = ResultSet.filter(BuildingName__range=(value[1][0], value[1][1]))
            else:
                ResultSet = ResultSet.filter(BuildingName__exact=value[1])
        elif key == "ConstructedYear":
            value = keywordDict[key]
            if value[0]:  # is a Range
                ResultSet = ResultSet.filter(ConstructedYear__range=(int(value[1][0]), int(value[1][1])))
            else:
                ResultSet = ResultSet.filter(ConstructedYear__exact=value[1])
        elif key == "Contractor":
            value = keywordDict[key]
            if value[0]:  # is a Range
                ResultSet = ResultSet.filter(ConstructedYear__range=(value[1][0], value[1][1]))
            else:
                ResultSet = ResultSet.filter(ConstructedYear__exact=value[1])
        elif key == "Floor":
            value = keywordDict[key]
            if value[0]:  # is a Range
                ResultSet = ResultSet.filter(Floor_range=(value[1][0], value[1][1]))
            else:
                ResultSet = ResultSet.filter(Floor__exact=value[1])
        elif key == "Shop":
            value = keywordDict[key]
            if value[0]:  # is a Range
                ResultSet = ResultSet.filter(Shop__range=(value[1][0], value[1][1]))
            else:
                ResultSet = ResultSet.filter(Shop__exact=value[1])
        elif key == "None":
            # try:
            #     value = int(keywordDict[key])
            # except:
            for child in keywordDict[key]:
                if not child[0]:
                    try:
                        val = int(child[1])
                        ResultSet = ResultSet.filter(Q(ConstructedYear__exact=val) |
                                                     Q(Floor__exact=val) |
                                                     Q(Shop__exact=val))
                    except:
                        val = child[1]
                        ResultSet = ResultSet.filter(Q(DrawingID__exact=val) |
                                                     Q(BuildingName__exact=val) |
                                                     Q(Contractor__exact=val))
        else:
            return "Failed"

    print(ResultSet)
    if not ResultSet:
        return "Failed"
    ResultJsonArray = []
    for child in ResultSet:
        ResultJsonObj = {}
        ResultJsonObj["DrawingID"] = child.DrawingID
        ResultJsonObj["BuildingName"] = child.BuildingName
        ResultJsonObj["ConstructedYear"] = child.ConstructedYear
        ResultJsonObj["Contractor"] = child.Contractor
        ResultJsonObj["Floor"] = child.Floor
        ResultJsonObj["Shop"] = child.Shop
        ResultJsonArray.append(ResultJsonObj)

    rtnSet = dict()
    rtnSet["rtnList"] = ResultJsonArray
    return json.dumps(rtnSet)