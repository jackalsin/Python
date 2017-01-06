def appearBefore(new,functionName): 
    # to check wheter this funtionname has appeared
    for item in functionName:
        if item == new:
            return True
    return False

def deleteDot(resultWithDot):
    # to delete the dot in the tail
    resultWithoutDot=""
    for i in range(len(resultWithDot)-1):
        resultWithoutDot+=resultWithDot[i]
    return resultWithoutDot

def findFuncion(position,code):
    # print("position and position+3",position,(position+3))
    if (code[position:(position+4)] =='def ' and code[position+5]=='('):
        return True
    else:
        return False

# print(findFuncion(0,"def f(x)=weoi"))

def tripleDoubleQuote(position,code):
    if position>(len(code)-3):
        return False
    elif (code[position:(position+3)] == '"""'):
        return True
    else:
        return False

def tripleSingleQuote(position,code):
    if position>(len(code)-3):
        return False
    if (code[position:(position+3)] == "'''"):
        return True
    else:
        return False

def doubleQuote(position,code):
    
    if (code[position] =='"' and (not(tripleDoubleQuote(position,code)))):
        return True
    else:
        return False

def singleQuote(position,code):
    if (code[position] =="'" and (not(tripleDoubleQuote(position,code)))):
        return True
    else:
        return False

def sharpSign(position,code):
    if (code[position]=="#"):
        return True
    else:
        return False

def topLevelFunctionNames(code):
    possibleFunctionName=""
    for position in range (len(code)):
        print("we are testing position", position,code[position])
        if findFuncion(position,code):
            print("position %d now is here 1" %(position))
            if (not (appearBefore(code[position+4],possibleFunctionName))):
                possibleFunctionName+=code[position+4]+'.'
            print(possibleFunctionName)

        elif tripleSingleQuote(position,code):
            print("position %d now is here 2" %(position))
            while (not(tripleSingleQuote(position,code))):
                position+=1
            position+=3

        elif tripleDoubleQuote(position,code): 
            print("position %d now is here 3" %(position))
            position+=1
            while(not(tripleDoubleQuote(position,code))):
                print("we enter the infinit loops")
                position+=1
            position+=3
                
        elif doubleQuote(position,code):
            print("position %d now is here 4" %(position))
            position+=1
            print("doubleQuote",position,code)
            while((doubleQuote(position,code))):
                position+=1

        elif singleQuote(position,code):
            print("position %d now is here 5" %(position))
            while(not(singleQuote(position,code))):
                position+=1

        elif sharpSign(position,code):
            print("position %d now is here 6" %(position))
            while(not(code[position]!='\n')):
                position+=1

    possibleFunctionName=deleteDot(possibleFunctionName)
    print("aaaaa",possibleFunctionName)
    return possibleFunctionName



def testTopLevelFunctionNames():
#     print("Testing topLevelFunctionNames()...", end="")
#     code = """\
# def f(x): return x+42
# def g(x): return x+f(x)
# def f(x): return x-42
# """
#     assert(topLevelFunctionNames(code) == "f.g")
    code = '''\
def f(): return """
def g(): pass"""
'''
    assert(topLevelFunctionNames(code) == "f")
    assert(topLevelFunctionNames(('def f(): return 42 # """\ndef g(): pass # """\n')))
    print("Passed. (Add more tests to be more sure!)")

testTopLevelFunctionNames()
