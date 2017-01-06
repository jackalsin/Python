# hw4.py
# Zhiwei Xin + zxin + AA


################Q1 
# count the first item of list a and remove this item for 'count' times
def lookAndSay(a):
    result=[]
    while(len(a)>0):
        count=a.count(a[0])
        result.append((count,a[0]))
        for j in range(count):
            a.remove(a[0])
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
    for c in word:
        if c not in hand:
            return False
    return True


def bestScarbbleScore(dictionary, letterScores,hand):
    bestScore=0

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

    return (bestWord,bestScore)

#########Question RunSimpleProgram
# A=list(range(124))
# L=list(range(124))

def getStatement(line): # to get a striped line into different elem
    statement=[]
    for item in line:
        statement.append(item)
    return statement
    

def getArgs(A,args):
    for i in range (len(args)):
        A[i]=args[i] # this is destructive

def returnArgsValue(item,A,L): # item A0
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
    
def assign(left,right): # L0 A0,args are string
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
                operand.append(statement[i])
            else: # operand is A0 
                operand.append(returnArgsValue(statement[i],A,L))
        rightEquation=str(operand[0])+statement[1]+str(operand[1])
        if statement[1]=='+':
            rightValue=operand[0]+operand[1]
        else:
            rightValue=operand[0]-operand[1]       
        modifyList(ListRef,index,rightValue,A,L)
    else:
        print('Something is wrong')
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
    A=[None]*124
    L=[None]*124
    getArgs(A,args)
    programLines=[]
    i=0
    for line in program.splitlines():
        programLines.append(line.strip()) # elimiate the initial spaces
    while(i<(len(program.splitlines()))): # len =5 and iMax = 4
        if (programLines[i].startswith('!')):
            i+=1
        elif (programLines[i].startswith('L')):
            assignStatement(programLines[i],A,L)
            i+=1
        elif (programLines[i].startswith('JMP ')): # JMP [label] jump to lable
            # do jump
            i+=1
        elif (programLines[i].startswith('JMP+')): # JMP+ [expr] [label]  
            statement=getStatement(programLines[i])
            if returnArgsValue(statement[1])>0:
                continue # turn on conditional Swith
            else:
                while(programLines[i].startswith(len(statement[2]))
                    ==statement[2]): # to find the label
                    i+=1
                i+=2 # from lable to the next next line, next is label statement
        elif (programLines[i].startswith('JMP0')):
            # do jump when expression
            return
        elif (programLines[i].startswith('RTN ')):
            # do return stuff
            return

    print("A=",A)
    print("L=",L)
program='''! hahah
 L0 13
 L1 + A0 32
 L3 - 32 A1
 '''
runSimpleProgram(program,[5,6])

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

    print("Passed. (Add more tests to be more sure!)")



def testBestScrabbleScore():
    dictionary=['abc','love',"David","Kosbie",'abcd']
    letterScores=[1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,1, 1, 3,10, 1, 1, 1, 1, 4, 4, 8, 4,10]
    hand=['a','b','c','l','o','v','e']
    print(bestScarbbleScore(dictionary,letterScores,hand))
    print("Testing bestScarbbleScore()...", end="")
    assert(bestScarbbleScore())

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
    print("Passed!")

def testAll():
    testLookAndSay()
    testInverseLookAndSay()
    testSolveCryptarithm()
    testLinearRegression()
    
if __name__ == "__main__":
    testAll()