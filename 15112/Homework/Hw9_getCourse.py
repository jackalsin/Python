import copy


def getCourse(courseCatalog, courseNumber):
    print()
    print("now checking catalog ", courseCatalog)
    if(type(courseCatalog[0]) == str ):
        if(courseNumber in courseCatalog):
            return courseCatalog[0] +'.' + courseNumber
        else: # not in 
            if(len(courseCatalog[1:])>0): # not the end 
                return getCourse(courseCatalog[1:],courseNumber)
            else:
                return None
    else:
        print("enter else")
        if(type(courseCatalog[0][0]) == str):
            return courseCatalog[0][0] + "." + getCourse(courseCatalog[1:],courseNumber)
        else: 
            return 
        result = getCourse(courseCatalog[1:], courseNumber)
        if (result == None):
            return None
        else:
            return courseCatalog[0] + '.' + result




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
    print(getCourse(courseCatalog,"18-100"))
    print()
    # print(getCourse(courseCatalog, "15-112"))
    # getCourse(courseCatalog, "99-307") 
    getCourse(courseCatalog, "15-213")

    print("passed")
    pass

testGetCourse()