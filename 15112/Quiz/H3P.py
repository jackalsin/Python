import string
def sameChars(s1,s2):
    for c in s1:
        # print("Now we are testing" ,c)
        if not c in s2:
            return False
    # print("it passes the first lab")
    for c in s2:
        # print("Now we are testing", c)
        if not c in s1:
            return False
    # print("it passes the second lab")
    return True
def wordWrap(text, width):
    count=0
    result=""
    for i in range (len(text)):
        count+=1
        # print(result)
        if text[i]==" ":
            # print("Now we are printting text and count", text[i-1], count,i,len(result))
            if text[i-1]!=" ":
                if (count-1)%4==0:
                    count-=1
                else:
                    result+='-'
                # print(result)
        else: 
            result+=text[i]
        if (count)%4==0 and result[-1]!='\n':
            result+='\n'

    # print(result)
    return result

def largestNumber(text):
    temp=0
    count=0
    large=0
    for i in text:
        if i >='0' and i <= '9':
            # print('Now printing i',ord(i))
            temp=ord(i)-48+temp*10
            # print("print temp after",temp)

        if (temp > large):
            large=temp
        if  (i<'0' or i>'9'):           
            temp=0
    if large:
        return large
    else:
        return None

def commonString(i,s1,s2):
    currentCommonString=''
    longestCommonString=''
    for j in range (len(s2)):
        if (s1[i]==s2[j]):
            k=j
            l=i
            while(s2[k]==s1[l] and k<len(s2) and l<len(s1)):
                currentCommonString+=s1[l]
                # print(currentCommonString,s1[l],s2[k])
                l+=1
                k+=1
            if (len(currentCommonString))>(len(longestCommonString)):
                longestCommonString=currentCommonString
        temp=""
    return longestCommonString


def longestSubpalindrome(s1,s2):
    s1=s1.lower()
    s2=s2.lower()
    # print(s1,s2)
    longestSub=""
    for i in range (len(s1)):
        if len(longestSub)<=len(commonString(i,s1,s2)):
            longestSub=commonString(i,s1,s2)
    return longestSub
# print(commonString(0,"abcdef", "abqrcdest"))
# print(longestSubpalindrome("abcdef", "abqrcdest"))

def frequent(k,s):
    count=0
    for i in range (len(s)):
        if s[i]==k:
            count+=1
    return count

def leastFrequentLetters(s):
    s=s.lower()
    leastFrequency=frequent('a',s)
    result=""
    for k in range (ord('a'),ord('z')+1):
        if frequent(chr(k),s)>0:
            if frequent(chr(k),s)<leastFrequency:
                leastFrequency=frequent(chr(k),s)
                result=chr(k)
            elif frequent(chr(k),s)==leastFrequency:
                result+=chr(k)
    return result

# print(leastFrequentLetters("aDq efQ? FB'daf!!!"))

def replace(s1,s2,s3):
    replaceBeforeDigit=s1.find(s2)
    beforePart=s1[:replaceBeforeDigit]
    afterPart=s1[(replaceBeforeDigit+len(s2)):]
    newString=beforePart+s3+afterPart
    return newString


# print(replace('I love you','love','hate'))

def encrypt(plaintext, password):
    encryptText=""
    upperText=plaintext.upper()
    if password!=password.lower():
        return "password must be all lowercase"
    for i in range(len(plaintext)):
        ShiftedNumber=ord(upperText[i])+ord(password[i])-ord('a')
        if ShiftedNumber>ord('Z'):
            ShiftedNumber-=26
        encryptText+=chr(ShiftedNumber)
    return encryptText


def decrypt(encryptText,password):
    plaintext=""
    if password!=password.lower():
        return "password must be all lowercase"
    for i in range (len(encryptText)):
        ShiftedNumber=ord(encryptText[i])-ord(password[i])+ord('a')
        # print(ShiftedNumber)
        if ShiftedNumber< ord('A'):
            ShiftedNumber+=26
        plaintext+=chr(ShiftedNumber)
    return plaintext

# print(encrypt('aaabz','asaab'))
# print(decrypt('ASABA','asaab'))
def isUpperAlphabet(character):
    if character >='A' and character<='Z':
        return True
    else:
        return False

def isLowerAlphabet(character):
    if character>='a' and character <= 'z' :
        return True
    else:
        return False

def encodeOffset(s, d):
    result=""
    for i in range (len(s)):
        ShiftedNumber=ord(s[i])
        if (isUpperAlphabet(chr(ShiftedNumber)) 
            or isLowerAlphabet(chr(ShiftedNumber))):
            ShiftedNumber+=d
            if isLowerAlphabet(s[i]):
                while(ShiftedNumber>ord('z') or ShiftedNumber<ord('a')):
                    if ShiftedNumber>ord('z'):
                        ShiftedNumber-=26
                    elif ShiftedNumber<ord('a'):
                        ShiftedNumber+=26
            else:
                ShiftedNumber+=d
                while(ShiftedNumber>ord('Z') or ShiftedNumber<ord('A')):
                    if ShiftedNumber>ord('Z'):
                        ShiftedNumber-=26
                    elif ShiftedNumber<ord('A'):
                        ShiftedNumber+=26
        result+=chr(ShiftedNumber)
    return result

# print(encodeOffset("af&iw",27))
def isSuit(s):
    if s=="C" or s=="D" or s=='H' or s=='S':
        return True
    else:
        return False
def isNumber(s):
    if ((s>='2' and s<='9') or s=='T' or s=='J' or s=='Q' 
        or s=='K' or s=='A'):
        return True
    else:
        return False
def isValidHand(s):
    if len(s)!=10:
        return False
    for i in range (0,len(s),2):
        if (not (isNumber(s[i]) and isSuit(s[i+1]))):
            return False
    return True

def isFlush(s):
    Numbers=""
    result=""
    for i in range (1,len(s)-2,2):
        if s[i]!=s[i+2]:
            return False
    return True

def getNumber(s):
    Numbers=""
    for i in range(0,len(s),2):
        Numbers+=s[i]
    return Numbers

def isRoyalFlush(s):
    if not isValidHand(s):
        return False
    else:
        royal='23456789TJQKA'
        Numbers=getNumber(s)
        for i in range (0,len(Numbers)):#s[i] to check if royal contains s[i]
            count=0
            royalPosition=royal.find(Numbers[i])
            if royalPosition>8: return False

            while (count<5):# to check 
                if Numbers[count]!=royal[royalPosition+count]:
                    return False
                count+=1
            return True
        return False
def hasPair(s):
    if not isValidHand(s):
        return False
    else:
        number=getNumber(s)
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[i]==s[j]:
                    return True
        return False
print(hasPair('JCJCTC2C5C'))
# print(isRoyalFlush('2D3D4D5D6D'))
# print(isFlush('JCJCTC2C5C'))
# print(isValidHand('JDJS2H2D5C'))
#######################testFunction######################

def testSameChars():
    print("Testing sameChars()...", end="")
    # assert(type(sameChars(0)) == int)
    assert(sameChars('abc','abc') == True)
    assert(sameChars('Abc','abc') == False)
    assert(sameChars('abcc','abc') == True)
    assert(sameChars('ab1c222','abc122') == True)
    print("Passed. (Add more tests to be more sure!)")

def testWordWrap():
    print("Testing wordWrap()...", end="")
    assert(wordWrap("abcdefghij", 4)  ==  """\
abcd
efgh
ij""")
    assert(wordWrap("a  b c de  fg",  4)  ==  """\
a-b
c-de
fg""")
    print("Passed. (Add more tests to be more sure!)")

def testAll():
    testSameChars()
    testWordWrap()

testAll()
