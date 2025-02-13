# Python - Inheritance
# Types of Inheritance
"""
Single Inheritance
Multiple Inheritance
Multilevel Inheritance
Hierarchical Inheritance
Hybrid Inheritance
"""


# 1. Python - Single Inheritance
# parent class
class Parent:
    def parentMethod(self):
        print("Calling parent method")


# child class
class Child(Parent):
    def childMethod(self):
        print("Calling child method")


# instance of child
c = Child()
# calling method of child class
c.childMethod()
# calling method of parent class
c.parentMethod()


# 2. Python - Multiple Inheritance
class Division:
    def __init__(self, a, b):
        self.n = a
        self.d = b

    def divide(self):
        return self.n / self.d


class Modulus:
    def __init__(self, a, b):
        self.n = a
        self.d = b

    def mod_divide(self):
        return self.n % self.d


class Div_mod(Division, Modulus):
    def __init__(self, a, b):
        self.n = a
        self.d = b

    def div_and_mod(self):
        divval = Division.divide(self)
        modval = Modulus.mod_divide(self)
        return (divval, modval)


x = Div_mod(10, 3)
print("division:", x.divide())
print("mod_division:", x.mod_divide())
print("divmod:", x.div_and_mod())


# 3. Python - Multilevel Inheritance
# parent class
class Universe:
    def universeMethod(self):
        print("I am in the Universe")


# child class
class Earth(Universe):
    def earthMethod(self):
        print("I am on Earth")


# another child class
class India(Earth):
    def indianMethod(self):
        print("I am in India")

    # creating instance


person = India()
# method calls
person.universeMethod()
person.earthMethod()
person.indianMethod()

# 4. Python - Hierarchical Inheritance
# parent class
class Manager:
    def managerMethod(self):
        print("I am the Manager")


# child class
class Employee1(Manager):
    def employee1Method(self):
        print("I am Employee one")


# second child class
class Employee2(Manager):
    def employee2Method(self):
        print("I am Employee two")

    # creating instances


emp1 = Employee1()
emp2 = Employee2()
# method calls
emp1.managerMethod()
emp1.employee1Method()
emp2.managerMethod()
emp2.employee2Method()

# 5. Python - Hybrid Inheritance
# parent class
class CEO:
    def ceoMethod(self):
        print("I am the CEO")


class Manager(CEO):
    def managerMethod(self):
        print("I am the Manager")


class Employee1(Manager):
    def employee1Method(self):
        print("I am Employee one")


class Employee2(Manager, CEO):
    def employee2Method(self):
        print("I am Employee two")

# creating instances
emp = Employee2()
# method calls
emp.managerMethod()
emp.ceoMethod()
emp.employee2Method()


# 6. Super() function
# parent class
class ParentDemo:
    def __init__(self, msg):
        self.message = msg

    def showMessage(self):
        print(self.message)


# child class
class ChildDemo(ParentDemo):
    def __init__(self, msg):
        # ParentDemo.__init__(self, msg) # Type-1
        # use of super function
        # super(ChildDemo, self).__init__(msg) # Type-2
        super().__init__(msg) # # Type-3

# creating instance
obj = ChildDemo("Welcome to Tutorialspoint!!")
print(obj.__dir__())
obj.showMessage()

