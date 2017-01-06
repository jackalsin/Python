def reverse(s,depth = 0):
    print(" " * depth,"reverse(",s,")")
    if len(s) == 0:
        result = ""
    else:
        result = reverse(s[1:],depth+1) + s[0]
    print(" "*depth, "--> result = ", result)
    return result 

print(reverse("wIlveoupiwewe2"))