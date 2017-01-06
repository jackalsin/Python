# hw4.py
# Zhiwei Xin + zxin + AA


################Q1 
# count the first item of list a and remove this item for 'count' times
import copy
def lookAndSay(a):
    aa=copy.copy(a)
    result=[]
    while(len(aa)>0):
        count=aa.count(aa[0])
        result.append((count,aa[0]))
        for j in range(count):
            aa.remove(aa[0])
    return result


def inverseLookAndSay(a):
    result=[]
    for i in range(len(a)):
        (count,item)=a[i] # get times and item, for loop
        for j in range(count):
            result.append(item)
    return result

def string2digit(string): # string number to int
    sum=0
    sign=1
    print("the string we are dealing with",string)
    if string[0]=='-':
        sign=-1
        string=string[1:]
    while(len(string)):
        digit=ord(string[0])-ord('0') # the first digit
        sum=sum*10+digit
        string=string[1:]
    return sign*sum

# to get a list like
# 0 to "O", 1 to "M", 2 to "Y", 5 to "E", 
# 6 to "N", 7 to "D", 8 to "R", and 9 to "S" 
def solution2List(solution): 
    result=[]
    for i in range(10):
        result.append(solution[i])
    return result

# make puzzle into 3-item list,alpha string
def puzzle2List(puzzle):
    plusPosition=puzzle.find('+')
    equalPosition=puzzle.find('=')
    result=[]
    result.append(puzzle[:plusPosition])
    result.append(puzzle[plusPosition+1:equalPosition])
    result.append(puzzle[equalPosition+1:])
    return result

def listFind(List, target): # to return the position of a certain item
    for i in range(len(List)):
        if List[i]==target:
            return i
# first check all the letters in the puzzle are in solution
# element in arguments are strings
def decode(puzzleList,solList): 
    result=[]
    for i in range(len(puzzleList)):
        temp=''
        for j in range(len(puzzleList[i])):
            index=listFind(solList,puzzleList[i][j])
            temp+=str(index)
        result.append(temp) # now we get a list of 3 stirng number
    for i in range(3):
        result[i]=string2digit(result[i])
    return result


def solvesCryptarithm(puzzle, solution):
    solList=solution2List(solution) # make solution into correspoding list
    puzzleList=puzzle2List(puzzle) # make puzzle into 3-item list,alpha string
    for i in range(len(puzzleList)): # to check all letters in solution
        for j in range(len(puzzleList[i])):
            if puzzleList[i][j] not in solList:
                return False
    additionList=decode(puzzleList,solList)
    # print(additionList)
    if (additionList[0]+additionList[1]==additionList[2]):
        return True
    else:
        return False
###########Q4
def almostEqual(x,y):
    return True if abs(x-y)<1e-8 else False

def getBar(a): # to get average of x and y
    sumX=sumY=0
    for i in range(len(a)):
        sumX+=a[i][0]
        sumY+=a[i][1]
    return sumX/len(a),sumY/len(a)

# print(getBar([(1,3),(2,5),(4,8)])) # test only

def getSS(a,xBar,yBar):
    SSxx=SSxy=0
    for i in range(len(a)):
        SSxx+=(a[i][0]-xBar)**2
        SSxy+=(a[i][0]-xBar)*(a[i][1]-yBar)
    return SSxx,SSxy

def getSSdev_res(a,xBar,yBar,k,b):
    sumDev=sumRes=0
    for i in range(len(a)):
        sumDev+=(a[i][1]-yBar)**2
        sumRes+=(a[i][1]-k*(a[i][0])-b)**2
    return ((sumDev-sumRes)/sumDev)**0.5

# print(getSS([(1,3),(2,5),(4,8)],2.3333333333333335, 5.333333333333333))

def linearRegression(a):
    xBar,yBar=getBar(a)
    SSxx,SSxy=getSS(a,xBar,yBar)
    k=SSxy/SSxx
    b=yBar-k*xBar
    R=getSSdev_res(a,xBar,yBar,k,b)
    return [k,b,R]



###### question 4
def getScore(word,letterScores):
    score=0
    while(len(word)):
        c=word[0]
        index=ord(c)-ord('a')
        score+=letterScores[index]
        word=word[1:]
    return score

def isValid(word,hand): # to check if the word letter is in hand
    handCopy=copy.copy(hand)
    for c in word:
        if c not in handCopy:
            return False
        handCopy.remove(c)
    return True


def bestScrabbleScore(dictionary, letterScores,hand):
    bestScore=0
    bestWord=[]
    for word in dictionary:
        if isValid(word,hand):
            currentWord=word
            currentScore=getScore(word,letterScores)
            if currentScore>bestScore:
                bestScore=currentScore
                bestWord=currentWord
            elif currentScore==bestScore:
                if type(bestWord)==list:
                    bestWord.append(currentWord)
                else:
                    bestWord=[bestWord,currentWord]
    if bestScore!=0:        
        return (bestWord,bestScore)
    else:
        return None

#########Question RunSimpleProgram
# A=list(range(124))
# L=list(range(124))

def getStatement(line): # to get a striped line into different elem
    statement=[]
    for item in line.split(' '):
        statement.append(item)
    return statement
    

def getArgs(A,args):
    for i in range (len(args)):
        A[i]=args[i] # this is destructive

def returnArgsValue(item,A,L): # item A0
    print("the item we are dealing with",item)
    ListRef=item[0]
    index=string2digit(item[1:])
    if index>=124 or index<0: 
        print("returnArgsValue goes Wrong")
    if ListRef=='A':
        return A[index]
    elif ListRef=='L':
        return L[index]
    else:
        print('returnArgsValue goes wrong on refering #####')

# print(returnArgsValue('L240'))
def modifyList(ListRef,index,value,A,L): #value must be digits, ListRef
    if ListRef=='A':
        A[index]=value
    else:
        L[index]=value
    
def assign(left,right,A,L): # L0 A0,args are string
    ListRef=left[0]
    index=string2digit(left[1:])
    if ((right[0]>='0' and right[0]<='9') or right[0]=='-'): # digit
        right=string2digit(right)
        modifyList(ListRef,index,right,A,L)
    else: # right is a Element
        rightListRef=right[0]
        rightListIndex=string2digit(right[1:])
        rightValue=returnArgsValue(right,A,L)
# assign("L37",'0')
# print(L)
def operandIsDigit(item):
    if ((item[0]>='0' and item[0]<='9') or
         item[0]=='-'):
        return True
    else:
        return False

def assignStatement(line,A,L): # L0 - A0 A1|| L0 A0||L0 1
    statement=[]
    for item in line.split(' '):
        statement.append(item)
    ListRef=statement[0][0]
    index=string2digit(statement[0][1:])
    if len(statement)==2: # L0 0||L0 A0
        if (operandIsDigit(statement[1])): # L0 0
            value=string2digit(statement[1])
        else: # L0 A0
            rightListRef=statement[1][0]
            rightListIndex=string2digit(statement[1][1:])
            value=returnArgsValue(statement[1])
        modifyList(ListRef,index,value,A,L)
    elif (len(statement)==4): # L0 - A0 A1
        operand=[]
        for i in range (2,4):
            if operandIsDigit(statement[i]): # operand is digits
                operand.append(string2digit(statement[i]))
            else: # operand is A0 
                operand.append(returnArgsValue(statement[i],A,L))
        print("Now we are printign operands",operand)
        if (statement[1]=='+'):
            rightValue=operand[0]+operand[1]
        else:
            rightValue=operand[0]-operand[1]
        modifyList(ListRef,index,rightValue,A,L)
    else:
        print('Something is wrong')

def evaluation(operator, operandList,A,L):
    operand=[]
    for c in operandList:
        if operandIsDigit(c): # operand is digits
            operand.append(string2digit(c))
        else: # operand is A0 
            operand.append(returnArgsValue(c,A,L))
    print(operand)
    if (operator=='+'):
        rightValue=operand[0]+operand[1]
    else:
        rightValue=operand[0]-operand[1]
    return rightValue
################### above assignment statement
# def JMPplus(programLines, A, L):
#     statement=[]
#     for item in programLines:
#         statement.append(item)

######## for test only
# assignStatement('A33 - A0 34')
# print(A)
######################

def runSimpleProgram(program,args):
    A=[0]*124
    L=[0]*124
    getArgs(A,args)
    programLines=[]
    i=0
    for line in program.splitlines():
        programLines.append(line.strip()) # elimiate the initial spaces
    print("how many lines we have",len(program.splitlines()))
    print()
    while(i<(len(program.splitlines()))): # len =5 and iMax = 4
        print("now we are dealing with i=",i)
        if (programLines[i].startswith('!')):
            i+=1
        elif (programLines[i].startswith('L')):
            print("Now we are in step 2",programLines[i])
            assignStatement(programLines[i],A,L)
            print("now after that ","i=",i)
            i+=1
        elif (programLines[i].startswith('JMP ')): # JMP [label] jump to lable
            statement=getStatement(programLines[i])
            while(programLines[i][:len(statement[1])]!=statement[1]):
                i=(i+1)%(len(program.splitlines())) # find the label
            i+=1
            print("we are jumping to i=",i)
        elif (programLines[i].startswith('JMP+')): # JMP+ [expr] [label]  
            statement=getStatement(programLines[i])
            print("!!now we are in the JMP+,I=",i,statement[2])
            if returnArgsValue(statement[1],A,L)>0:
                while(programLines[i][:len(statement[2])]!=statement[2]):
                     # to find the label
                    i=(i+1)%(len(program.splitlines())) # in case of labe before
                print("the label is at",i)
                i+=1 # from lable to the next line
            else:
                i+=1 # three lines inclusive can shorted to i+=1
            print("we are jumping to i=",i)
        elif (programLines[i].startswith('JMP0')): # JMP0 [expr] [label]
            statement=getStatement(programLines[i])
            expr=returnArgsValue(statement[1],A,L)
            if expr==0:
                while(programLines[i][:len(statement[2])]!=statement[2]): 
                # to find the label
                    i=(i+1)%(len(program.splitlines())) # in case of labe before
            i+=1
        elif (programLines[i].startswith('RTN ')): # RTN [expr]
            statement=getStatement(programLines[i])
            print("we are dealing with returning satement", statement)
            if len(statement)==2:
                if operandIsDigit(statement[1]): # operand is digits
                    returnValue=(string2digit(statement[1]))
                else: # operand is A0 
                    returnValue=returnArgsValue(statement[1],A,L)
            else: #'RTN + 42 L42', [])
                returnValue=evaluation(statement[1],
                    [statement[2],statement[3]],A,L)
            return returnValue
        elif (programLines[i]==''): # if triple quote is theonly content
            i+=1
        else:
            i+=1
    print("A=",A)
    print("L=",L)

#######################test Function##################
program="""! largest: Returns max(A0, A1)
                   L0 - A0 A1
                   JMP+ L0 a0
                   RTN A1
                   a0:
                   RTN A0"""

print("Final result",runSimpleProgram(program,[6,5]))

sumToN = """! SumToN: Returns 1 + ... + A0
            ! L0 is a counter, L1 is the result
            L0 0
            L1 0
            loop:
            L2 - L0 A0
            JMP0 L2 done
            L0 + L0 1
            L1 + L1 L0
            JMP loop
            done:
            RTN L1"""

print("runSumtoN",runSimpleProgram(sumToN, [10]))
######################## test function end #################

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) == [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)])
    print("Passed. (Add more tests to be more sure!)")

def testInverseLookAndSay():
    print("Testing inverseLookAndSay()...", end="")
    assert(inverseLookAndSay(([])) == [])
    assert(inverseLookAndSay([(3,1)]) == [1,1,1])
    assert(inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7])
    assert(inverseLookAndSay([(3,1)]) == [1,1,1])
    assert(inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10])
    print("Passed. (Add more tests to be more sure!)")

def testString2digit():
    print("Testing string2digit()...", end="")
    assert(string2digit('0') == 0)
    assert(string2digit('-123') == -123)
    assert(string2digit('323') == 323)
    assert(string2digit('383828830') == 383828830)
    print("Passed. (Add more tests to be more sure!)")

def testSolution2List():
    print("Testing solution2List()...", end="")
    assert(solution2List('OMY--ENDRS') 
        == ['O', 'M', 'Y', '-', '-', 'E', 'N', 'D', 'R', 'S'])
    assert(solution2List('OMYWOWOERS') 
        == ['O', 'M', 'Y', 'W', 'O', 'W', 'O', 'E', 'R', 'S'])
    assert(solution2List('----------') 
        == ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'])
    print("Passed. (Add more tests to be more sure!)")

def testDecode():
    print("Testing decode()...", end="")
    assert(decode(['MORE','AND','MORE'],['O', 'M', 
        'Y', 'A', '-', 'E', 'N', 'D', 'R', 'S'])==[1085, 367, 1085])
    assert(decode(['WE','LIKE','KOSBIE'],
        ['W', 'E', 'L', 'I', 'K', '-', 'O', 'S', 'B', 'I'])==[1, 2341, 467831])
    assert(decode(['WE','HATE','KOSBIE'],
        ['W', 'E', 'H', 'A', 'K', 'T', 'O', 'S', 'B', 'I'])==[1, 2351, 467891])

    print("Passed. (Add more tests to be more sure!)")

def testSolveCryptarithm():
    print("Testing solvesCryptarithm()...", end="")
    assert(solvesCryptarithm('SEND+MORE=MONEY','OMY--ENDRS') == True)
    assert(solvesCryptarithm('CABD+EEF=CDCE','-EF--B-CAD') == True)
    assert(solvesCryptarithm('CABD+EEF=CDCE','-EF--B-C-D') == False)
    assert(solvesCryptarithm('CABD+ETF=CDCE','-EF--B-C-D') == False)
    print("Passed. (Add more tests to be more sure!)")

def testLinearRegression():
    print("Testing linearRegression()...", end="")
    assert(linearRegression([(1,3),(2,5),(4,8)])==
         [1.6428571428571432, 1.4999999999999987, 0.997176464952738])
    assert(linearRegression([(1,3),(12,5),(4,18),(3,3),(323,44)])==
         [0.11545377748576001, 6.679870864476864, 0.9340026651859771])
    assert(linearRegression([(1,2),(2,3)])==[1.0, 1.0, 1.0])

    print("Passed. (Add more tests to be more sure!)")



def testBestScrabbleScore():
    dictionary=['abc','love',"David","Kosbie",'abcd']
    letterScores=[1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,1, 1, 
    3,10, 1, 1, 1, 1, 4, 4, 8, 4,10]
    hand=['a','b','c','l','o','v','e']
    # print(bestScarbbleScore(dictionary,letterScores,hand))
    print("Testing bestScrabbleScore()...", end="")

    assert(bestScrabbleScore(dictionary,letterScores,hand)
        ==((['abc', 'love'], 7)))
    dictionary2=['abc',"David","Kosbie",'abcd']
    # print(hand,bestScrabbleScore(dictionary2,letterScores,
        # ['a','b','c','l','o','v','e']),)
    assert(bestScrabbleScore(dictionary2,letterScores,
        ['a','b','c','l','o','v','e'])
        ==('abc', 7))
    print(bestScrabbleScore(['xyz', 'zxy', 'zzy', 'yy', 'yx', 'wow'], 
        [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 
        2, 3, 4, 5, 1], ['x', 'y', 'z']))
    assert(bestScrabbleScore(['xyz', 'zxy', 'zzy', 'yy', 'yx', 'wow'], 
        [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 
        2, 3, 4, 5, 1], ['x', 'y', 'z']) == (['xyz', 'zxy'], 10))
    assert(bestScrabbleScore(['xyz', 'zxy', 'zzy', 'yy', 'yx', 'wow'], 
        [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 
        4, 5, 1], ['w', 'x', 'z'])==None)
    assert(bestScrabbleScore(['a', 'b', 'c'], [1, 1, 1, 1, 1, 1, 1, 1, 1, 
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], ['z'])==None)
    print("Passed. (Add more tests to be more sure!)")


def testRunSimpleProgram():
    print("Testing runSimpleProgram()...", end="")
    largest = """! largest: Returns max(A0, A1)
                   L0 - A0 A1
                   JMP+ L0 a0
                   RTN A1
                   a0:
                   RTN A0"""
    assert(runSimpleProgram(largest, [5, 6]) == 6)
    assert(runSimpleProgram(largest, [6, 5]) == 6)

    sumToN = """! SumToN: Returns 1 + ... + A0
                ! L0 is a counter, L1 is the result
                L0 0
                L1 0
                loop:
                L2 - L0 A0
                JMP0 L2 done
                L0 + L0 1
                L1 + L1 L0
                JMP loop
                done:
                RTN L1"""
    assert(runSimpleProgram(sumToN, [5]) == 1+2+3+4+5)
    assert(runSimpleProgram(sumToN, [10]) == 10*11//2)
    assert(runSimpleProgram('RTN 42',[]) == 42)
    assert(runSimpleProgram('JMP foo\nRTN 1\nfoo:\nRTN 2', []) == 2)
    assert(runSimpleProgram('RTN L42', []) == 0)
    assert(runSimpleProgram('RTN + 42 L42', [])==42)
    print("Passed!")
    
def testPuzzle2List():
    print("Testing puzzle2List()...", end="")
    assert(puzzle2List('SEND+MORE=MONEY')==['SEND', 'MORE', 'MONEY'])
    assert(puzzle2List('GAVE+MORE=MONEY')==['GAVE', 'MORE', 'MONEY'])
    assert(puzzle2List('GAVE+MORE=MWEOE')==['GAVE', 'MORE', 'MWEOE'])

    print("Passed. (Add more tests to be more sure!)")

def testGetStatement():
    print("Testing getStatement()...", end="")
    assert(getStatement("L0 - A0 A1")==['L0', '-', 'A0', 'A1'])
    assert(getStatement('JMP0 L2 done')==['JMP0', 'L2', 'done'])
    assert(getStatement('RTN L1')==['RTN', 'L1'])

    print("Passed. (Add more tests to be more sure!)")

def testGetArgs():
    print("Testing getArgs()...", end="")
    A=[0]*124
    getArgs(A,[33,23])
    assert(A[0]==33 and A[1]==23)
    A=[0]*124
    getArgs(A,[])
    assert(A[0]==0)
    A=[0]*124
    getArgs(A,[11])
    assert(A[0]==11)
    print("Passed. (Add more tests to be more sure!)")

def testReturnArgsValue():
    print("Testing returnArgsValue()...", end="")
    A=list(range(124))
    L=list(range(124))
    assert(returnArgsValue('A0',A,L)==0)
    assert(returnArgsValue('A123',A,L)==123)
    assert(returnArgsValue('L15',A,L)==15)
    print("Passed. (Add more tests to be more sure!)")

def testModifyList():
    print("Testing returnArgsValue()...", end="")
    A=list(range(124))
    L=list(range(124))
    modifyList('L',11,27,A,L)
    assert(L[11]==27)
    modifyList('L',27,44,A,L)
    assert(L[27]==44)
    modifyList('A',0,88,A,L)
    assert(A[0]==88)
    print("Passed. (Add more tests to be more sure!)")


def testAssignStatement():
    
    print("Testing assignStatement()...", end="")
    A=list(range(124))
    L=[17]*124
    assignStatement('A33 - A0 34',A,L)
    assert(A[33]==-34)
    assignStatement('L123 + A0 34',A,L)
    assert(L[123]==34)
    assignStatement('L98 + A0 L93',A,L)
    assert(L[98]==17)
    print("Passed. (Add more tests to be more sure!)")

def testEvaluation():
    evaluation(operator, operandList,A,L)

    print("Testing evaluation()...", end="")
    A=list(range(124))
    L=[17]*124
    assert(evaluation('-',[A0,23],A,L)== -23)
    assert(evaluation('+',[44,23],A,L)== 67)
    assert(evaluation('+',[44,L2],A,L)== 61)
    print("Passed. (Add more tests to be more sure!)")

def testAll():
    testLookAndSay()
    testInverseLookAndSay()
    testSolveCryptarithm()
    testLinearRegression()
    testBestScrabbleScore()
    testRunSimpleProgram()

    ###### help Function###########
    testString2digit()
    testSolution2List()
    testPuzzle2List()
    testDecode()
    testGetStatement()
    testGetArgs()
    testReturnArgsValue()
    testModifyList()
    testAssignStatement()

if __name__ == "__main__":
    testAll()