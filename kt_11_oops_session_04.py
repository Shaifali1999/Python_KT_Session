# 1. Python - Polymorphism
# Ways of implementing Polymorphism in Python
"""
Duck Typing
Operator Overloading
Method Overriding
Method Overloading
"""

# 1.1 Duck Typing
"""
You can call any method on an object without checking its type
"""


class Duck:
    def sound(self):
        return "Duck ==> Quack, quack!"


class AnotherBird:
    def sound(self):
        return "AnotherBird==> I'm similar to a duck!"


def makeSound(get_obj):
    print(get_obj.sound())


# creating instances
duck = Duck()
anotherBird = AnotherBird()
print(f"Duck obj: {duck}")
print(f"anotherBird obj: {anotherBird}")
# calling methods
makeSound(duck)
makeSound(anotherBird)


# 2 Operator Overloading
class Vector:
    def __init__(self, a, b):
        # v1 = Vector(2, 10)
        self.a = a
        self.b = b

    def __str__(self):
        return f'@@__STR__ ===> Vector ({self.a}, {self.b}) @@\n'

    def __add__(self, other):
        print(f"Other: {other}")
        # print("##__ADD___==> ", other, self.a, self.b, "##\n")
        # v1 = Vector(2, 10) self.a =2, self.b=10
        # v2 = Vector(5, -2) other.a=5, other.b=-2
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, 2)
# 1st v1 object is called, then v2 object will call __add__ method and send that v2 object into that "other" parameter
c = v1 + v2
# Object: Call __str__ method
print(c)


# 2.1 Method Overloading
class Example:
    def add(self, a, b):
        x = a + b
        return x

    def add(self, a, b, c):
        x = a + b + c
        return x


obj = Example()
print(obj.add(10, 20, 30))


# print(obj.add(10, 20))  # Will raise TypeError: Example.add() missing 1 required positional argument: 'c'

# TypeError ==> Fix for the overloading

class Example:
    def add(self, a=None, b=None, c=None):
        x = 0
        if a != None and b != None and c != None:
            x = a + b + c
        elif a != None and b != None and c == None:
            x = a + b
        return x


obj = Example()
print(obj.add(10, 20, 30))
print(obj.add(10, 20))


class shape:
    def draw(self):
        print("draw method")
        return


class circle(shape):
    def draw(self):
        print("Draw a circle")
        return


class rectangle(shape):
    def draw(self):
        print("Draw a rectangle")
        return


shapes = [circle(), rectangle()]
for shp in shapes:
    shp.draw()

