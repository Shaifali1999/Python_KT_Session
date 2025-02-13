# 1. Python Variable Scope
# Types of Scope for Variables in Python
"""
1. Local Variables
2. Global Variables
3. Nonlocal Variables
"""


# 1.1 Local Variables
def myfunction():
    a = 10
    b = 20
    print("variable a:", a)
    print("variable b:", b)
    return a + b


print(myfunction())

# 1.2 Global Variables
name = 'Tutorials'
marks = 50


def myfunction():
    # accessing inside the function
    print("name:", name)
    print("marks:", marks)


# function call
myfunction()

# 1.3 Nonlocal Variables
def yourfunction():
   a = 5
   b = 6
   # nested function
   def myfunction():
      # nonlocal function
      nonlocal a
      nonlocal b
      a = 10
      b = 20
      print("variable a:", a)
      print("variable b:", b)
      return a+b
   print (myfunction())
yourfunction()


# 2. Namespace and Scope of Python Variables
'''
1. Built-in namespace
2. Global namespace
3. Local namespace
'''

print(globals())

# 2.1 Python globals() Function
name = 'TutorialsPoint'
marks = 50
result = True

def myfunction():
    a = 10
    b = 20
    return a + b

print(globals())

# 2.2 Python locals() Function
name = 'TutorialsPoint'
marks = 50
result = True
def myfunction():
   a = 10
   b = 20
   c = a+b
   print ("globals():", globals())
   print ("locals():", locals())
   return c
myfunction()

