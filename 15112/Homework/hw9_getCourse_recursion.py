# hw9 getCourse
import copy


def getCourse(courseCatalog, courseNumber):
    # print()
    # print("now checking catalog ", courseCatalog)
    def getCourseInner(courseCatalog,courseNumber):
        if(type(courseCatalog[0]) == str ):
            # print("enter if")
            if(courseNumber in courseCatalog):
                # return courseCatalog[0] +'.' + courseNumber
                return courseNumber
            else: # not in 
                if(len(courseCatalog[1:])>0): # not the end 
                    return getCourseInner(courseCatalog[1:],courseNumber)
                else:
                    return None
        else:
            # print("enter else")

            result = getCourseInner(courseCatalog[0], courseNumber)
            # print("result = ",result, "courseCatalog[0] ", courseCatalog[0])
            if (type(courseCatalog[0][0])==list): 
                return result
            if (result != None):
                # print("should enter")
                return courseCatalog[0][0] + '.' +result
                # return result
            # result == None
            elif (len(courseCatalog) == 1): # reach the end 
                return None

            else:
                resultIn = getCourseInner(courseCatalog[1:],courseNumber)
                if(resultIn == None):return None
                else:
                    return resultIn
    result = getCourseInner(courseCatalog,courseNumber)
    if result != None: return courseCatalog[0] + '.' + result
    else: return None 
        # elif (len(courseCatalog) == 1):
        #     return courseCatalog[0] + '.' + result

        # elif (getCourse(courseCatalog[1:]))
        # else:
        #     return courseCatalog[0] + '.' + result




def testGetCourse():
    print("getCourse()...")#,end = "")
    courseCatalog = ["CMU",
                        ["CIT",
                            [ "ECE", "18-100", "18-202", "18-213" ],
                            [ "BME", "42-101", "42-201" ],
                        ],
                        ["SCS",
                            [ "CS", 
                              ["Intro", "15-110", "15-112" ],
                              "15-122", "15-150", "15-213"
                            ],
                        ],
                        "99-307", "99-308"
                    ]
    print("final result = ",getCourse(courseCatalog,"18-100"))
    print()
    print(getCourse(courseCatalog, "15-112"))
    print(getCourse(courseCatalog, "99-307") )
    print(getCourse(courseCatalog, "15-213"))

    print(getCourse(courseCatalog,"33"))

    print("passed")
    pass

testGetCourse()