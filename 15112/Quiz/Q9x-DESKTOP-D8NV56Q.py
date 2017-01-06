def fib(n,depth = 0):
    if (n<2):
        result = 1
        print("    "*depth, "f(", n,")")
        return result
    else:
        print("    "*depth, "f(",n,")")
        result = fib(n-1,depth+1) + fib(n-2,depth + 1)
        
        return result

print(fib(8))