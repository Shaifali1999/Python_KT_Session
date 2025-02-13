# 1. Python - Access Modifiers
"""
Public members − A class member is said to be public if it can be accessed from anywhere in the program.
Protected members − They are accessible from within the class as well as by classes derived from that class.
    * To imply that a certain instance variable is protected, prefix it with single underscore (such as "_salary").
Private members − They can be accessed from within the class only.
    * To indicate that an instance variable is private, prefix it with double underscore (such as "__age").
"""


class Employee:
    def __init__(self, name, age, salary):
        self.name = name  # public variable
        self._salary = salary  # protected variable
        self.__age = age  # private variable

    def displayEmployee(self):
        print("I am from parent==> Name : ", self.name, ", age: ", self.__age, ", salary: ", self._salary)


# e1 = Employee("Bhavana", 24, 10000)
# e1.displayEmployee()
# print(e1.name)
# print(e1._salary)
# # print(e1.__age)     # AttributeError: 'Employee' object has no attribute '__age'


class Child(Employee):
    def __init__(self, name, age, salary):
        self.name = name  # public variable
        self._salary = salary  # protected variable
        self.__age = age  # private variable
        super().__init__(name, age, salary)

    def displayEmployee(self):
        print("I am from child==> Name : ", self.name, ", age: ", self.__age, ", salary: ", self._salary)


cls_obj = Child('A', 25, '10k')
cls_obj.displayEmployee()
print(cls_obj.name)
print(cls_obj._salary)
# print(cls_obj.__age)  # AttributeError: 'Child' object has no attribute '__age'

# 2. Python - Name Mangling
"""
obj._class__privatevar
print (e1._Employee__age)
"""

# 3. Python - Property Object
"""
property(fget=None, fset=None, fdel=None, doc=None)
"""


# 3.1 Getters and Setter Methods without property
class Employee:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__abc = '1'

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_abc(self):
        print("called get_abc")
        return self.__abc

    def set_name(self, name):
        self.__name = name
        return

    def set_age(self, age):
        self.__age = age

    def set_var(self, abc):
        self.__abc = abc


e1 = Employee("Bhavana", 24)
print("Name:", e1.get_name(), "age:", e1.get_age())
e1.set_name("Archana")
e1.set_age(21)
print("Name:", e1.get_name(), "age:", e1.get_age())
e1.set_var('500')
print("Name:", e1.get_name(), "age:", e1.get_age(), 'abc: ', e1.get_abc())


# 3.2 Using Property
class Employee:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name
        return

    def set_age(self, age):
        self.__age = age
        return

    name = property(get_name, set_name, "name")
    age = property(get_age, set_age, "age")


e1 = Employee("Bhavana", 24)
print("Name:", e1.name, "age:", e1.age)

e1.name = "Archana"
e1.age = 23
print("Name:", e1.name, "age:", e1.age)


# 3.3 Using @property decorator
class Portal:

    # Defining __init__ method
    def __init__(self):
        self.__name = ''

    # Using @property decorator, @property is by default Getter method so no need to mention that name.getter
    @property
    # Getter method
    def name(self):
        return self.__name

    # Setter method
    @name.setter
    def name(self, val):
        self.__name = val

    # Deleter method
    @name.deleter
    def name(self):
        del self.__name


# Creating object
p = Portal()

# Setting name
p.name = 'Sriram'
# Prints name
print(p.name)
# Deletes name
del p.name
# As name is deleted above this
# will throw an error
# print(p.name)
