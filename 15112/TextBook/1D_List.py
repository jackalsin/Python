import string
def collapseWhitespace(s):
    result=''
    if len(s)==1:
        if s in string.whitespace:
            return ' '
        else:
            return s

    for i in range(len(s)-1):
        if s[i] not in string.whitespace:
            result+=s[i]
        if s[i] in string.whitespace and s[i+1] not in string.whitespace:
            result+="X"
    if s[len(s)-1] in string.whitespace and s[len(s)-2] not in string.whitespace:
        result+='X'
    return result

print(collapseWhitespace("  a\n\n\nb   "))
print(collapseWhitespace(" "))
print(collapseWhitespace("b"))