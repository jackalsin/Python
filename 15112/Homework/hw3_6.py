# first we a fuction to determine whether the object is in a string

# a function whether it's a three quotes
def tripleSingleDetection(position, line):
    # to return how many triple before position '''
    count=0
    for k in range(0,position):
        if (line[k] == "'" and line[k+1] == "'" and line[k+2] == "'" ):
            count+=1
    return count 

# print(tripleSingleDetection(15,'"""ojiweojiwoejfowje''wooweiowe"'))

def tripleDoubleDetection(position, line):
# a function return how many triple double quote """
    count=0
    for k in range(0,position):
        if (line[k] == '"' and line[k+1] == '"' and line[k+2] == '"'):
            count+=1
    return count 

# print(tripleDoubleDetection(15,'"""ojiweojiwoejfowje''wooweiowe"'))

# a function wheter it's a two quotes
def doubleDetection(position, line):
# a function return how many double quote: "   "
    count=0
    for k in range (0,position): 
        print(line[k])
        if line[k]=='"' :
            print("Now we testing",k)
            if k==0 and line[k+1]=='"' and line[k+2]=='"':
                print("when k=0 we enter here1")
                continue
            elif (k==1 and ((line[k-1]=='"' and line[k+1]=='"') or 
                (line[k+1]=='"' and line[k+2]=='"'))):
                print("when k=1 we enter here2")
                continue
            elif ((line[k-2] =='"' and line[k-1] =='"') or (line[k-1] =='"' 
                and line[k+1] =='"') or (line[k+2] =='"' and line[k+1] =='"')):
                print("when k=%d we enter here3" %(k))
                continue
            else:
                print("when k=%d we enter here4" %(k))
                count+=1                
    return count
print(len("""sf"sf"w'efwefwefwefw"""))
s="""sf"sf"w'efwefwefwefw"""
print(s[19])
print(doubleDetection(19, """sf"sf"wefw"efwefwef"w"""))

def singleDetection(position,line):
# a function wheter it's a one quotes
    count=0
    # if not(tripleDoubleDetection(position,line)):
    for k in range (0,position): 
        if line[k]=="'" :
            if k==0 and line[k+1]=="'" and line[k+2]=="'":
                print("when k=0 we enter here")
                continue
            elif (k==1 and ((line[k-1]=="'" and line[k+1]=="'") or 
                (line[k+1]=="'" and line[k+2]=="'"))):
                print("when k=1 we enter here")
                continue
            elif ((line[k-2] =="'" and line[k-1] =="'") or (line[k-1] =="'" 
                and line[k+1] =="'") or (line[k+2] =="'" and line[k+1] =="'")):
                print("when k=%d we enter here" %(k))
                continue
            else:
                print("when k=%d we enter here" %(k))
                count+=1 
    return count

# print(singleDetection(15, """sf"sf"w'ef'wefwefwefw"""))


def deleteComment(line):
    result=""
    for item in line:
        if item == '#':
            break
        else:
            result+=item
    return result

def deleteDot(resultWithDot):
    # to delete the dot in the tail
    resultWithoutDot=""
    for i in range(len(resultWithDot)-1):
        resultWithoutDot+=resultWithDot[i]
    return resultWithoutDot

def isOdd(number):
    if number%2==1:
        return True
    else:
        return False

def topLevelFunctionNames(code):
    possibleFunctionName=''
    result=''
    doubleQuoteNumbersBeforeThisLine=0 # to record triple double quote
    doubleQuoteNumbersAfterThisLine=0
    singleQuoteNumbersBeforeThisLine=0 # to record triple single quote
    singleQuoteNumbersAfterThisLine=0
    tripleDoubleQuoteNumberBeforeThisLine=0
    tripleDoubleQuoteNumberAfterThisLine=0
    tripleSingleQuoteNumberBeforeThisLine=0
    tripleSingleQuoteNumberAfterThisLine=0
    for line in code.splitlines():

        # take care of comments
        sharpPosition=findSharp(line)
        if (not((isOdd(sharpPosition)) or (isOdd(sharpPosition)) 
            or (isOdd(sharpPosition)))):
            line=deleteComment(line)

    # try to extract a line 
    # to check whether it's in a string
    # check if it start with "def "
        # if so,
# once ran into a "#", go to check above three functions

    # if not in a string: execute the deleteComment

    #
