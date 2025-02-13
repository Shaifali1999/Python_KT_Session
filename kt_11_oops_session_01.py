# Python OOPS
"""
Class
Object
Encapsulation
Inheritance
Polymorphism
"""


# 1. defining class
class Smartphone:
    kumar = '13'

    # constructor
    def __init__(self, device, brand):
        self.device = device
        self.brand = brand

    # method of the class
    def description(self):
        print("Print my class var: ", self.kumar)
        print("try to print with name: ", Smartphone.kumar)
        return f"{self.device} of {self.brand} supports Android 14"


# creating object of the class
phoneObj = Smartphone("Smartphone", "Samsung")
print("phoneObj: ", phoneObj)
ret_val = phoneObj.description()
print("ret_val: ", ret_val)


# 2. Encapsulation

class Desktop:
    def __init__(self):
        self.__max_price = 25000
        self.muthu = '200'

    def sell(self):
        return f"Selling Price: {self.__max_price}, own var: {self.muthu}"

    def set_max_price(self, price):
        if price > self.__max_price:
            self.__max_price = price


# Object
desktopObj = Desktop()
print(desktopObj.sell())
# print(desktopObj.__max_price) # AttributeError: 'Desktop' object has no attribute '__max_price'. Did you mean: 'set_max_price'?

# modifying the price directly
desktopObj.__max_price = 35000
print(desktopObj.sell())

# Update muthu variable
desktopObj.muthu = "500"
print(desktopObj.sell())

# modifying the price using setter function
desktopObj.set_max_price(35000)
print(desktopObj.sell())


# 3. Inheritance
# define parent class
class Parent:
    parentAttr = 100

    def __init__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print("Calling parent method")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Parent attribute :", Parent.parentAttr)


# define child class
class Child(Parent):
    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print("Calling child method")


# instance of child
c = Child()
# child calls its method
c.childMethod()
# calls parent's method
c.parentMethod()
# again call parent's method
c.setAttr(200)
# again call parent's method
c.getAttr()


# 4. Polymorphism
# You can always override your parent class methods.
# define parent class
class Parent:
    def myMethod(self):
        print("Calling parent method")


# define child class
class Child(Parent):
    def myMethod(self):
        print("Calling child method")


# instance of child
c = Child()
# child calls overridden method
c.myMethod()


# 4.1 Instance attribute vs Class attributes
class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.age = 18
        Employee.empCount += 1

    def displayCount(self):
        self.sriram = None
        """
        Instance attribute is accessed using the object name followed by dot notation.
        """
        # print(Employee.name) # AttributeError: type object 'Employee' has no attribute 'name'
        print(self.name)
        """
        Class attributes can be accessed by both class name and object name.
        """
        print("Total Employee %d" % Employee.empCount)
        print("Total Employee_2time %d" % self.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


cls_obj = Employee("A", 10000)
cls_obj.displayEmployee()
cls_obj.displayCount()

cls_obj = Employee("B", 5000)
cls_obj.displayEmployee()
cls_obj.displayCount()

cls_obj = Employee("C", 40000)
cls_obj.displayEmployee()
cls_obj.displayCount()

# Returns true if 'age' attribute exists
if hasattr(cls_obj, 'age'):
    # Returns value of 'age' attribute
    print("GET before delete: ", getattr(cls_obj, 'age'))
    # Delete attribute 'age'
    delattr(cls_obj, 'age')
    # Returns value of 'age' attribute
    # print("GET after delete", getattr(cls_obj, 'age')) # AttributeError: 'Employee' object has no attribute 'age'
else:
    # Set attribute 'age' at 8
    setattr(cls_obj, 'age', 8)
    # Returns value of 'age' attribute
    print("GET as new value: ", getattr(cls_obj, 'age'))

# =======================================================================

# Python - Class Methods
"""
We can divide Python methods in three different categories, which are class method, instance method and static method.
"""


# 1. Using classmethod() Function
class Employee:
    empCount = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Employee.empCount += 1

    def showcount(self):
        print(self.empCount)

    counter = classmethod(showcount)


e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)

e1.showcount()
Employee.counter()


# 2. Using @classmethod Decorator

class Employee:
    empCount = 0

    def __init__(self, name, age, addr=None):
        self.name = name
        self.age = age
        self.addr = addr
        Employee.empCount += 1

    @classmethod
    def showcount(cls):
        print(cls.empCount)

    @classmethod
    def newemployee(cls, name, age):
        return cls(name, age, "Bang")

    def displayDetails(self):
        print(f"Name: {self.name}, Age: {self.age}, Addr: {self.addr}")


e1 = Employee("Bhavana", 24)
e1.displayDetails()

e2 = Employee("Rajesh", 26)
e2.displayDetails()

e3 = Employee("John", 27)
e3.displayDetails()

e4 = Employee.newemployee("Anil", 21)
e4.displayDetails()

Employee.showcount()


# 3. Access Class Attributes in Class Method

class Cloth:
    # Class attribute
    price = 4000

    @classmethod
    def showPrice(cls):
        return cls.price


# Accessing class attribute
print(Cloth.showPrice())


# 4. Dynamically Add Class Method to a Class
class Cloth:
    pass


# class method
@classmethod
def brandName(cls):
    print("Name of the brand is Raymond")


# adding dynamically
# Set (Class-Name, future Method on Cloth, already we have standalone @class-method)
setattr(Cloth, "brand_name", brandName)
newObj = Cloth()  # Without setattr ==> AttributeError: 'Cloth' object has no attribute 'brand_name'
newObj.brand_name()


# 5. Static Method in Python(without self and cls)
class Student:
    stdCount = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Student.stdCount += 1

    # creating staticmethod
    @staticmethod
    def showcount():
        print(Student.stdCount)


e1 = Student("Bhavana", 24)
e2 = Student("Rajesh", 26)
e3 = Student("John", 27)

print("Number of Students:")
Student.showcount()


# 6. Python - Instance Methods

class Employee:
    def __init__(self, name="Bhavana", age=24):
        self.name = name
        self.age = age

    def displayEmployee(self):
        print("Name : ", self.name, ", age: ", self.age)


e1 = Employee()
e2 = Employee("Bharat", 25)

e1.displayEmployee()
e2.displayEmployee()
