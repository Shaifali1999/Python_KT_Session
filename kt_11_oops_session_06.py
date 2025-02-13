# 1. Python - Inner Classes
class Student:
    def __init__(self):
        self.name = "Ashish"
        self.subs = self.Subjects()
        return

    def show(self):
        print("Name:", self.name)
        self.subs.display()

    class Subjects:
        def __init__(self):
            self.sub1 = "Phy"
            self.sub2 = "Che"
            return

        def display(self):
            print("Subjects:", self.sub1, self.sub2)


s1 = Student()
s1.show()


# 2. Python - Anonymous Class and Objects
class myclass:
    def __init__(self):
        self.myvar = 10
        return


obj = myclass()

print('class of int', type(int))
print('class of list', type(list))
print('class of dict', type(dict))
print('class of myclass', type(myclass))
print('class of obj', type(obj))


# 3. Anonymous Class and Object Example
# anon=type('', (object, ), {})
def getA(self):
    return self.a


obj = type('', (object,),
           {'a': 5, 'b': 6, 'c': 7, 'getA': getA, 'getB': lambda self: self.b, 'getC': lambda self: self.c})()
print(obj.getA(), obj.getB(), obj.getC())


# 4. Python - Wrapper Classes
def decorator_function(get_class):
    class Wrapper:
        def __init__(self, x):
            self.wrap = get_class(x)

        def print_name(self):
            return self.wrap.name, self.wrap.abc

    return Wrapper


@decorator_function
class Wrapped:
    def __init__(self, x):
        self.name = x
        self.abc = [1, 3]


cls_obj = Wrapped('TutorialsPoint')
ret_val_1, ret_val_2 = cls_obj.print_name()
print(f"ret_val: {ret_val_1}, {ret_val_2}")


# 5. Decorator - Nested Function
def outer(x):
    def inner(y):
        return x + y

    # var = inner(9)
    return inner


add_five = outer(5)
print(f"add_five: {add_five}")
result = add_five(6)
print(f"Example - 5 ==> result: {result}")  # prints 11


# 6. Decorator - Pass Function as Argument
def add(x, y):
    return x + y


def calculate(muthu, x, y):
    print(f"Type: {type(muthu)}")
    ret = muthu(x, y)  # add function name as muthu
    return ret


result = calculate(add, 4, 6)
print(f"Example - 6 ==> {result}")  # prints 10


# 7 Python Decorators with @
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Args: {args}, Kwargs: {kwargs}")
        # # Call the original function
        result = func(*args, **kwargs) # def execute_func(name):
        print(f"Executed on actual function: {result}")
        # Convert the result to uppercase
        conv_upper = result.upper()
        print("Inside wrapper")
        return conv_upper

    print(f"I am inside uppercase_decorator function before calling the wrapper_name: {func}")
    return wrapper


# Using the decorator
@uppercase_decorator
def execute_func(name):
    print("I am inside execute_func before concatenation line")
    local_var = f"Hello, {name}!"
    print("I am inside execute_func after concatenation line")
    return local_var


# Testing the decorated function
ret_op = execute_func("Muthukumar")  # Output: HELLO, MUTHUKUMAR!
print(f"ret_op: {ret_op}")
