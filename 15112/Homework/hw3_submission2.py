#Homework Exercise 3!!!! Name: Zhiwei Xin Andrew ID: zxin
import string

def almostEqual(x,y):
    return True if abs(x-y)<1e-8 else False

def isAWhitespace(c): #if c is a whitespace, return false; else : true
    if c == " ":
        return True
    else:
        return False

def deleteSpace(s): #to delete the space in string
    result=""
    for c in s:
        if c != " ":
            result+=c
    return result

def patternedMessage(message,patterned):
    result=""
    count=0
    for c in patterned: 
        # print(result)
    # check every charater in patterned and copy to another
        if isAWhitespace(c):
            result+=' '
        elif (c=='\n'):# start a new line
            result+='\n'
        else: # not a whitespace
            #if message has a space....Deal with it
            message=deleteSpace(message)
            result+=message[count%(len(message))]
            count+=1
    # print(result)
    return result


#############################Question 2####################
def reverseString(s):
    return s[::-1]

def extractString(message, jRow,rows):
# get jrow's string in original order
# j\i 0 1 2 3
 # 0  W T A W
 # 1  E A T N
 # 2  A C D
 # 3  T K A
    result=""
    temp=""
    count=0
    maxCol=maxColFunction(message,rows)
    for iCol in range (maxCol):
        if (iCol*rows +jRow)<len(message):
            temp=message[iCol*rows +jRow]
            result+=temp 
    return result

# print(extractString("WEATTACKATDAWN",3,4))
def outputNumber2String(rows):
    result=""
    while(rows):
        result+=chr(rows%10+ord('0'))
        rows//=10
    result=reverseString(result)
    return result
# print(outputNumber2String(41))

def maxColFunction(message,rows):
    possibleMaxCol=len(message)/rows
    if almostEqual(possibleMaxCol,round(possibleMaxCol)):
        # if possible Max Col is an integer
        # print("lenstest1",len(message),rows)
        return round(possibleMaxCol)
    else:
        # not an integer
        # print("lenstest2",len(message),rows)
        possibleMaxColNotInteger=(len(message))//rows+1
        return possibleMaxColNotInteger
# print(maxColFunction("WEFWWSWSGWWEF",3))

def encodeRightLeftCipher(message, rows):
    count=0 #for z y x 
    result=outputNumber2String(rows)
    maxCol=maxColFunction(message, rows)
    for jRow in range(rows):
        temp=extractString(message,jRow,rows)
        # print("temp=",temp)
        if len(temp)<maxCol:
            temp+=chr(ord('z')-count) # put z,y,x in
            count+=1
        if jRow%2==1: # reverse it 
            temp=reverseString(temp)
        result+=temp
    return result

# print(encodeRightLeftCipher("WEATTACKATDAWN",4))
############################## Question 3 ###########
def string2Digit(gradeString): #get a grade in string format, but a integer output
    number=0
    signBit=1
    for c in gradeString:
        if c=='-':
            signBit=-1
        else:
            number=number*10+ord(c)-ord('0')
    return signBit*number

def getEnconded(encodedMessage):
    result=""
    for i in range (1,len(encodedMessage)):
        result+=encodedMessage[i]
    return result

def maxRowFunction(message,cols):
    possibleMaxRow=round(len(message)/cols)
    return possibleMaxRow

def getIRow(encodeLetters,iRow,cols):
    start=iRow*cols
    end=iRow*cols+cols-1
    result=""
    for i in range (start,end+1):
        result+=encodeLetters[i]
    return result

# print(getIRow("WADACEAKWNATTTz",1,5))

def extractColomn(encodeLetters,jCol,cols):
# get iRow's string in the corresponding order
    result=""
    temp=""
    maxRow=maxRowFunction(encodeLetters,cols)
    for iRow in range (maxRow):
        iRowLine=getIRow(encodeLetters,iRow,cols)
        if iRow%2==1: # do the reverse thing
            iRowLine=reverseString(iRowLine) 
        # print("iRowLine",iRowLine)
        temp=iRowLine[jCol]
        if not (ord(temp)<=ord('z') and ord(temp)>=ord('a')):
            result+=temp 
    return result

# print(extractColomn("WADACEAKWNATTTz",1,5))

def decodeRightLeftCipher(encodedMessage):
    cols=string2Digit(encodedMessage[0]) 
    encodeLetters=getEnconded(encodedMessage)
    # print("cols and encodeLetters", cols, encodeLetters)
    result=""
    temp=""
    for jCol in range(cols):
        temp=extractColomn(encodeLetters,jCol,cols)
        # print(temp)
        result+=temp
    return result

# print(decodeRightLeftCipher("5WADACEAKWNATTTz"))

############################## Question 4 ###########



def bestAverageFunction(currentName,currentAve,bestName,bestAverage): 
    # to compare which one is best
    if currentAve>=bestAverage:
        return currentName, currentAve
    else:
        return bestName,bestAverage

def digit2String(grade):
    if not (grade):
        return "0"
    absGrade=abs(grade)
    result=""
    while(absGrade):
        # print("absGrade = ",absGrade)
        result+=chr(absGrade%10+ord('0'))
        absGrade//=10
    result=reverseString(result)
    if grade<0:
        result='-'+result
    return result

# print(digit2String(-3928))
def isDigit(item):
    for c in item:
        if (ord(c)>= ord('0') and ord(c)<=ord('9')) or c=='-':
            return True
        else:
            return False
         
def bestStudentAndAvg(gradebook):
    bestName=""
    bestAverage=-100
    currentName=""
    currentAve=0
    for line in gradebook.splitlines():
        count=0 # how many grades he has
        sumOfGrades=0
        # print("We reach the first point", line)
        if line=="" or line.startswith("#"): 
        # if line.startswith("#"): 
            # ignore the blank line and starting with #
            # print("we once entered here")
            continue
        # print("we enter the second",line)
        for item in line.split(","):
            # print("item",item)
            if not isDigit(item):
                # print("Now we are entering item.isdigit",item)
                currentName=item;
                # print('currentName =', currentName)
                continue
            else:
                sumOfGrades+=string2Digit(item)
                count+=1
        currentAve=sumOfGrades/count
        currentAve= round(currentAve)
        # print("currentAve",currentAve)
        bestName,bestAverage=bestAverageFunction(currentName,
            currentAve,bestName,bestAverage)
        # print("Average = ",bestName, bestAverage)
    bestAverageString=digit2String(bestAverage)
    return bestName+":"+ bestAverageString


###################### Question 5 ##############################

def findTripleQuote(line): 
    # to return numbers of the triple quotes
    count=0
    for i in range(len(line)):
        if i > (len(line)-3): 
        # neglect the last two character and the character behind #
            break
        elif(line[i]=='"' and line[i+1]=='"' and line[i+2]=='"'):
            count+=1
    return count

def isOdd(number):
    if number%2==1:
        return True
    else:
        return False
def isEven(number):
    if number%2==0:
        return True
    else:
        return False

def getStringFromStart2End(line,start,end):
    # to get a string from line ,beginning with line[start], 
    # ending with line[end]
    result=""
    for i in range (start,end):
        result+=line[i]
    return result

def appearBefore(line,functionName): 
    # to check wheter this funtionname has appeared
    for item in line.split('.'):
        if item == functionName:
            return True
    return False

# print("Testing",appearBefore("f.g.",'h'))
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

def topLevelFunctionNames(code):
    possibleFunctionName=''
    result=''
    quoteNumbersBeforeThisLine=0 # to record triple double quote
    quoteNumbersAfterThisLine=0
    singleQuoteNumbersBeforeThisLine=0 # to record triple single quote
    singleQuoteNumbersAfterThisLine=0
    for line in code.splitlines():
        # print("we are with line", line)
        line=deleteComment(line)# delete #
        quoteNumbersBeforeThisLine=quoteNumbersAfterThisLine
        quoteNumbersAfterThisLine+=findTripleQuote(line)
        singleQuoteNumbersBeforeThisLine=singleQuoteNumbersAfterThisLine
        singleQuoteNumbersAfterThisLine+=findTripleQuote(line)
        # print("before and AfterThisLine", quoteNumbersBeforeThisLine,quoteNumbersAfterThisLine)
        if line.startswith("def "):
            functionNameStrat=line.find("def ")+len("def ")
            functionNameEnd=line.find('(')
            possibleFunctionName=getStringFromStart2End(line,functionNameStrat,
            functionNameEnd)
            # print("functionName",possibleFunctionName,quoteNumbersBeforeThisLine) 
            ### to see whether it's in the triple quote
            if (isOdd(quoteNumbersBeforeThisLine) or isOdd(singleQuoteNumbersBeforeThisLine)):
                # print("we enter quoteNumbers")
                continue
            # to determine whether it appeared before
            # print("appearBefore",result, "possibleFunctionName",possibleFunctionName,appearBefore(result,possibleFunctionName))
            if not appearBefore(result,possibleFunctionName):
                # print("appearBefore",result, possibleFunctionName)
                result+=possibleFunctionName+'.'
                # print(result)
    result=deleteDot(result) # delete the dot at the tail
    # print("nothing Else")
    return result

code = "def f(): return '''\ndef g(): pass'''\n"

print(topLevelFunctionNames(code))


############################## Test Function ##############


def testIsAWhitespace():
    print("Testing isAWhitespace()...", end="")
    assert(isAWhitespace(" ") == True) 
    assert(isAWhitespace("2") == False)
    assert(isAWhitespace("a") == False)
    print("Passed. (Add more tests to be more sure!)")

def testDeleteSpace():
    print("Testing deleteSpace()...", end="")
    assert(deleteSpace(" ") == "") 
    assert(deleteSpace("I hate cats") == "Ihatecats")
    assert(deleteSpace("Kosbie rocks") == 'Kosbierocks')
    print("Passed. (Add more tests to be more sure!)")

def testPatternedMessage():
    print("Testing patternedMessage()...", end="")
    assert(patternedMessage('12345','## ### ####### ###') 
        == '12 345 1234512 345') 
    assert(patternedMessage('324313','') 
        == '') 
    assert(patternedMessage("Go Pirates!!!", """
***************
******   ******
***************
""") == """
GoPirates!!!GoP
irates   !!!GoP
irates!!!GoPira
""")
    assert(patternedMessage("Three Diamonds!","""
    *     *     *
   ***   ***   ***
  ***** ***** *****
   ***   ***   ***
    *     *     *
""") == '''
    T     h     r
   eeD   iam   ond
  s!Thr eeDia monds
   !Th   ree   Dia
    m     o     n
''')
    assert(patternedMessage("Go Steelers!",
"""
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ '$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
'$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  '$$$
   '$$$'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$o
   o$$'   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$' '$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$'$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$'
 ''''       $$$$    '$$$$$$$$$$$$$$$$$$$$$$$$$$$$'      o$$$
            '$$$o     '$$$$$$$$$$$$$$$$$$'$$'         $$$
              $$$o          '$$'$$$$$$'           o$$$
               $$$$o                                o$$$'
                '$$$$o      o$$$$$$o'$$$$o        o$$$$
                  '$$$$$oo     '$$$$o$$$$$o   o$$$$'
                     '$$$$$oooo  '$$$o$$$$$$$$$'
                        '$$$$$$$oo $$$$$$$$$$
                                '$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$'
                                      '$$$'
""")
 == '''
                          GoSteelers!GoSteeler
                      s!GoSteelers!GoSteelers!GoS
                   teelers!GoSteelers!GoSteelers!GoS         te   el er
   s ! Go        Steelers!GoSteelers!GoSteelers!GoSteel       er s! GoSt
ee l e rs      !GoSteeler    s!GoSteelers!    GoSteelers       !GoSteel
ers!GoSte     elers!GoSt      eelers!GoSt      eelers!GoSt    eelers!G
  oSteele    rs!GoSteele      rs!GoSteele      rs!GoSteelers!GoSteeler
  s!GoSteelers!GoSteelers    !GoSteelers!G    oSteelers!GoSt  eele
   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSteel     ers!
    GoS   teelers!GoSteelers!GoSteelers!GoSteelers!GoSteelers     !GoSt
   eele   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSt       eele
   rs!    GoSteelers!GoSteelers!GoSteelers!GoSteelers!Go Steelers!GoSteele
  rs!GoSteelers  !GoSteelers!GoSteelers!GoSteelers!GoS   teelers!GoSteelers
  !GoSteelers!G   oSteelers!GoSteelers!GoSteelers!Go     Steel
 ers!       GoSt    eelers!GoSteelers!GoSteelers!G      oSte
            elers     !GoSteelers!GoSteelers!         GoS
              teel          ers!GoSteel           ers!
               GoSte                                elers
                !GoSte      elers!GoSteele        rs!Go
                  Steelers     !GoSteelers!   GoStee
                     lers!GoSte  elers!GoSteeler
                        s!GoSteele rs!GoSteel
                                ers!GoSteele
                                    rs!GoSteeler
                                     s!GoSteeler
                                      s!GoS
''')
    print("Passed. (Add more tests to be more sure!)")

def testExtractString():
    print("Testing extractString()...", end="")
    assert(extractString("WEATTACKATDAWN",1,4) == "EATN") 
    assert(extractString("WEATTACKATDAWN",0,4) == "WTAW")
    assert(extractString("WEATTACKATDAWN",0,5) == "WAD")
    print("Passed. (Add more tests to be more sure!)")
def testEncodeRightLeftCipher():
    
    print("Testing encodeRightLeftCipher()...", end="")
    assert(encodeRightLeftCipher("WEATTACKATDAWN",4) == "4WTAWNTAEACDzyAKT") 
    assert(encodeRightLeftCipher("WEATTACKATDAWN",5) == "5WADACEAKWNATTTz")
    assert(encodeRightLeftCipher("WEFWWSWSGWWEF",3) == "3WWWWFzWSWEFSGEy")
    print("Passed. (Add more tests to be more sure!)")
    

def testDecodeRightLeftCipher():
    print("Testing decodeRightLeftCipher()...", end="")
    assert(decodeRightLeftCipher("4WTAWNTAEACDzyAKT") == "WEATTACKATDAWN") 
    assert(decodeRightLeftCipher("5WADACEAKWNATTTz") == "WNAAWTDKTAATCE")
    assert(decodeRightLeftCipher("3WWWWFWWSWEFSGEz") ==  "WWWSGWFSFEWWWE")
    print("Passed. (Add more tests to be more sure!)")

def testBestStudentAndAvg():
    print("Testing bestStudentAndAvg()...", end="")
    assert(bestStudentAndAvg("""
# ignore  blank lines and lines starting  with  #'s
wilma,91,93
fred,80,85,90,95,100
betty,88
""") == "wilma:92") 
    assert(bestStudentAndAvg("""
# ignore  blank lines and lines starting  with  #'s
wilma,-1,93
fred,80,85,90,95,100
betty,88
""") == "fred:90")
    assert(bestStudentAndAvg("""
# ignore  blank lines and lines starting  with  #'s
wilma,91,93
fred,80,85,90,95,100
betty22,88
""") == "wilma:92")
    assert(bestStudentAndAvg('fred,0') == "fred:0")
    assert(bestStudentAndAvg('fred,-1\nwilma,-2')=="fred:-1")
    print("Passed. (Add more tests to be more sure!)")


def testFindTripleQuote():
    print("Testing findTripleQuote()...", end="")
    assert(findTripleQuote('"""woeio"""fwowwe """') == 3) 
    assert(findTripleQuote('"""232893"""fwow"we """') == 3)
    assert(findTripleQuote('"""232893"""fwow"w,e """') == 3)
    assert(findTripleQuote('') == 0)
    print("Passed. (Add more tests to be more sure!)")

def testGetStringFromStart2End():
    print("Testing getStringFromStart2End()...", end="")
    assert(getStringFromStart2End('Kosbierocks',3,3) == "") 
    assert(getStringFromStart2End('Kosbierocks',3,4) == "b")
    assert(getStringFromStart2End('I love #',0,5) == "I lov")
    assert(getStringFromStart2End('',0,0) == "")
    print("Passed. (Add more tests to be more sure!)")

def testTopLevelFunctionNames():
    print("Testing topLevelFunctionNames()...", end="")
    code = """\
def f(x): return x+42
def g(x): return x+f(x)
def f(x): return x-42
"""
    assert(topLevelFunctionNames(code) == "f.g")
    code = '''\
def f(): return """
def g(): pass"""
'''
    assert(topLevelFunctionNames(code) == "f")
    assert(topLevelFunctionNames(('def f(): return 42 # """\ndef g(): pass # """\n')))
    print("Passed. (Add more tests to be more sure!)")

def testAll():
    testIsAWhitespace()
    testDeleteSpace()
    testExtractString()
    testPatternedMessage()
    testEncodeRightLeftCipher()
    testDecodeRightLeftCipher()
    testBestStudentAndAvg()
    testFindTripleQuote()
    testGetStringFromStart2End()
    testTopLevelFunctionNames()

testAll()










