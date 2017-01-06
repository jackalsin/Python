def hasConsecutiveDigits(n):
    # Write the function hasConsecutiveDigits(n) that takes a possibly-negative 
    # integer n and returns True if n has two consecutive equal digits, 
    # and False otherwise. 
    while (n):
        Next=(n//10)%10
        if Next==(n%10):
            return True
        n=n//10
    return False



print(hasConsecutiveDigits(12))