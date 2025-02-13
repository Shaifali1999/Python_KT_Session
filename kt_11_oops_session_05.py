# 1. Python - Abstraction
"""
Abstract Method Overriding
Moreover, the class must have at least one abstract method.
"""
from abc import ABC, abstractmethod


class Democlass(ABC):
    @abstractmethod
    def method1(self):
        print("abstract method")
        return

    def method2(self):
        print("concrete method")


class Concreteclass(Democlass):
    def method1(self):
        print("Concreteclass==>method1 before ")
        super().method1()
        print("Concreteclass==>method1 after ")
        return

    # def muthu(self):
    #     print("Concreteclass==>method1 before ")
    #     super().method1()
    #     print("Concreteclass==>method1 after ")
    #     return


obj = Concreteclass()
obj.method1()
# obj.muthu()
obj.method2()

"""
Formal Interface
Informal Interface
"""

# 1. Formal Interface
"""
Formal interfaces in Python are implemented using abstract base class (ABC). To use this class, 
you need to import it from the abc module.
"""

from abc import ABC, abstractmethod


# creating interface
class demoInterface(ABC):
    @abstractmethod
    def method1(self):
        print("Abstract method1")
        return

    @abstractmethod
    def method2(self):
        print("Abstract method1")
        return


# class implementing the above interface
class concreteclass(demoInterface):
    def method1(self):
        print("This is method1")
        return

    def method2(self):
        print("This is method2")
        return


# creating instance
obj = concreteclass()

# method call
obj.method1()
obj.method2()

# 2. Informal Interface
"""
In Python, the informal interface refers to a class with methods that can be overridden. However, 
the compiler cannot strictly enforce the implementation of all the provided methods.
"""


class demoInterface:
    def displayMsg(self):
        pass


class newClass(demoInterface):
    def displayMsg(self):
        print("This is my message")


# creating instance
obj = newClass()

# method call
obj.displayMsg()
