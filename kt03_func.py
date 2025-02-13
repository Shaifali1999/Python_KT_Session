# 1. Function with return value
def func1():
    print("Hi, Im from func1()")
    return True


x = func1()
print(x)


# 2. Function with conditional statements.
def function_name(param):
    "function_docstring"
    if param == "Sriram":
        return True
    else:
        return False


function_name("Sriram")


# 3. Function with conditional statements and Dict
def function_name_1(param):
    "function_docstring"
    return_boolean = False
    if param == "Sriram":
        rvalue = func1()
        print("Calling the function1 ", rvalue)
        if rvalue is True:
            return_boolean = True
        else:
            return_boolean = False
    else:
        return_boolean = False

    dict_1 = {1: "Sriram",
              'Muthu': 'IB001',
              'kumar': {
                  'Dep': 'IT',
                  'Location': "Bang"
              }
              }
    return return_boolean, dict_1


value, ret_dict = function_name_1("Sriram3")
print("Returned Value is: ", value)
print("Returned Dict: ", ret_dict)
print("Display Kumar Details: ", ret_dict['kumar'], "\nDisplay IT:", ret_dict['kumar']['Dep'])

# 4. ShallowCopy and DeepCopy
import copy

# 4.1 Normal_Copy
old_list_nc = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list_nc = old_list_nc

# When we assign another list, id changes and it equates to deepcopy
# new_list_nc=[[1, 1, 1], [2, 2, 2], [3, 3, 3],[4, 4, 4]]
new_list_nc[1][1] = 10

print("Old list_nc:", old_list_nc, id(old_list_nc))
print("New list_nc:", new_list_nc, id(new_list_nc))

# 4.2 Shallow_Copy
old_list_c = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list_c = copy.copy(old_list_c)

new_list_c.append([4, 4, 4])
new_list_c[1][1] = 'A'

print("Old list_c:", old_list_c, id(old_list_c))
print("New list_c:", new_list_c, id(new_list_c))

# 4.3 Deep_Copy
old_list_dc = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list_dc = copy.deepcopy(old_list_dc)

new_list_dc.append([4, 4, 4])
new_list_dc[1][1] = 'A'

print("Old list_dc:", old_list_dc, id(old_list_dc))
print("New list_dc:", new_list_dc, id(new_list_dc))

# 5. Local Scope
num = 5


def testfunction(arg, num):
    print("Before", num)
    num = 7
    print("After", num)
    # print ("ID inside the function:", id(arg))


var = "Hello"
print("ID before passing:", id(var))
testfunction(var, num)
print("After--func ", num)

# 5.1 Global scope
num_2 = 5


def testfunction(arg):
    global num_2
    print("Before", num_2)
    num_2 = 7
    print("After", num_2)
    # print ("ID inside the function:", id(arg))


var = "Hello"
print("ID before passing:", id(var))
testfunction(var)
print("After--func ", num_2)


# 6. Function with arguments
def posFun(**m):
    # def posFun(a, *, b, num1, num2, num3):
    print(m)


l = [1, 2, 3]
d = {'a': 7,
     'b': 8}

# posFun(d)
posFun(**d)

for key_and_value in d:
    print("Key and Value is(Without .items()): ", key_and_value, d[key_and_value])

for key, value in d.items():
    print("Key and Value is(With .items() and with unpack of key,value pair): ", key, value)

for key_and_value in d.items():
    print("Key and Value is(With .items() and without unpack(tuple)): ", key_and_value, d[key_and_value[0]])


# 7. Function Annotations

def myfunction(a: int, b: int) -> int:
    c = a + b
    return c


print(myfunction(56, 88))
print(myfunction.__annotations__)
return_val = myfunction(56, 66)
print(type(return_val))

# 8. Types of Python Function Arguments
""" 
Refer more
Positional or Required Arguments
Keyword Arguments
Default Arguments
Positional-only Arguments
Keyword-only arguments
Arbitrary or Variable-length Arguments
"""


def func1(a, b, /, *args):
    sum = a + b
    for i in args:
        sum = sum + i
    print(sum)


func1(5, 4, 3, 2, 1, 0)


def func1(a, b=5, **kwargs):
    sum = a + b
    print(sum)
    print(kwargs)
    for i in kwargs:
        print(kwargs[i])


func1(5, 4, state="TN", city="Chennai")

# ===================================================
