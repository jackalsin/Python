#Chapter 3 Data and Expressions

#Some Builtin Types
import math
def f():
    print("This is a user-defined function")
    return 42

print("Some basic types in Python:")
print(type(2))           # int
print(type(2.2))         # float
print(type("2.2"))       # str  (string)
print(type(2 < 2.2))     # bool (boolean)
print(type(math))        # module
print(type(math.tan))    # builtin_function_or_method ("function" in Brython)
print(type(f))           # function (user-defined function)
print(type(type(42)))    # type

print("#####################################################")

print("And some other types we will see later in the course...")
print(type(Exception())) # Exception
print(type(range(5)))    # range
print(type([1,2,3]))     # list
print(type((1,2,3)))     # tuple
print(type({1,2}))       # set
print(type({1:42}))      # dict (dictionary or map)
print(type(2+3j))        # complex  (complex number) (we may not see this type)

#Task 6
print(3 * 2)
print(3 * "abc")
print(3 + 2)
print("abc" + "def")



#Task 9
print('\nTask 9\n')
print("The problem....")
d1 = 0.1 + 0.1 + 0.1
d2 = 0.3
print(d1 == d2)                # False (never use == with floats!)

print()
print("The solution...")
epsilon = 10**-10
print(abs(d2 - d1) < epsilon)  # True!

print()
print("Once again, using a useful helper function, almostEqual:")

def almostEqual(d1, d2):
    epsilon = 10**-10
    return (abs(d2 - d1) < epsilon)

d1 = 0.1 + 0.1 + 0.1
d2 = 0.3
print(d1 == d2)            # still False, of course
print(almostEqual(d1, d2)) # True, and now packaged in a handy reusable function!
