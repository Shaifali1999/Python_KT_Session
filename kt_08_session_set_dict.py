# 1. Python Set
"""
In Python, a set is an unordered collection of unique elements.
Unlike lists or tuples, sets do not allow duplicate values i.e.
each element in a set must be unique. Sets are mutable,
"""

# Accessing Values in Tuples
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])
l = [1, 2, 3, 4, 5, 6, 7]
print("l[0]: ", l[0])
print("l[1:5]: ", l[1:5])

# Updating Tuples Concatenation
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
# Following action is not valid for tuples
# tup1[0] = 100 # TypeError: 'tuple' object does not support item assignment
# So let's create a new tuple as follows
tup3 = tup1 + tup2
print(tup3)

# Delete Tuple Elements
tup = ('physics', 'chemistry', 1997, 2000)
print(tup)
del tup
tup = ('physics', 'chemistry', 1997, 2000)
print("After deleting tup : ")
print(tup)

# Unpack Tuple Items Using Asterisk (*)
tup1 = (10, 20, 30)
x, *y = tup1
print("x: ", "y: ", x, y)

# Joining Tuples Using List Comprehension
# new_list = [expression for item in iterable]

# Two tuples to be joined
T1 = (36, 24, 3)
T2 = (84, 5, 81)
# Joining the tuples using list comprehension
joined_tuple = [k for each_item in [T1, T2] for k in each_item]

joined_tuple_1 = [item for item in [T1, T2]]
print("joined_tuple_1: ", joined_tuple_1)

new_tup = []
for subtuple in [T1, T2]:
    print("subtuple: ", subtuple)
    for item in subtuple:
        new_tup.append(item)
new_tup = tuple(new_tup)
print("Non-comprehension method: {}".format(new_tup))

# Printing the joined tuple
print("Joined Tuple:", joined_tuple)

# Set - set define
my_set = {1, 2, 3, 4, 5}
print(my_set)

# Define set with typecasting
my_set = set([1, 2, 3, 4, 5])
print(my_set)

# Duplicate Elements in Set
my_set = {1, 2, 2, 3, 3, 4, 5, 5}
print(my_set)

mixed_set = {1, 'hello', (1, 2, 3)}
# [2, 5] TypeError: unhashable type: 'list'
# {5, 6} TypeError: unhashable type: 'set'
# {1: '3', 's': 10} TypeError: unhashable type: 'dict'
print(mixed_set)

# Adding Elements in a Set
my_set = {1, 2, 3, 3}
# Adding an element 4 to the set
my_set.add(4)
print(my_set)

# Removing Elements from a Set
my_set = {1, 2, 3, 4, 'hello'}
# Removes the element 3 from the set
my_set.remove('hello')
# my_set.remove('world') # KeyError: 'world'
print(my_set)

my_set = {1, 2, 3, 4}
# No error even if 5 is not in the set
my_set.discard(5)
print(my_set)

# Membership Testing in a Set
my_set = {1, 2, 3, 4}
if 2 in my_set:
    print("2 is present in the set")
else:
    print("2 is not present in the set")

# Set Operations
"""
Union − It combine elements from both sets using the union() function or the | operator.
Intersection − It is used to get common elements using the intersection() function or the & operator.
Difference − It is used to get elements that are in one set but not the other using the difference() function or the - operator.
Symmetric Difference − It is used to get elements that are in either of the sets but not in both using the symmetric_difference() method or the ^ operator.
"""

# Python Set Comprehensions
# set_variable = {expression for item in iterable if condition}
# Input is Set vlaues
squared_set = {x for x in range(1, 6) if x % 2 != 0}
print("squared_set- odd: ", squared_set)
squared_set = {x for x in range(1, 6) if x % 2 == 0}
print("squared_set: even", squared_set)

# Input is List vlues
squared_set = {x for x in [1, 2, 3, 1, 2, 3, 6, 5, 6, 8] if x % 2 == 0}
print("squared_set: even", squared_set)

# 2. Python Frozen Sets
"""
a frozen set is an immutable collection of unique elements, 
similar to a regular set but with the distinction that it cannot be modified after creation.
"""

my_frozen_set = frozenset([1, 2, 3])
print(my_frozen_set)
# my_frozen_set.add(4) # AttributeError: 'frozenset' object has no attribute 'add'  ==> immutable

# 3. Dictionaries in Python
# In Python, a dictionary is a built-in data type that stores data in key-value pairs.
# It is an unordered, mutable, and indexed collection.

d1 = {"Fruit": ["Mango", "Banana"], "Flower": ["Rose", "Lotus"]}
d2 = {('India, USA'): 'Countries', ('New Delhi', 'New York'): 'Capitals'}
print(d1)
print(d2)

d3 = {1: 2,
      2: 'abc',
      (3, 4): 'xyz',  # Dont use
      5: 'xyz-12_3',
      '23': 10,
      '145': '200',
      '173': 'abc300',
      '12qwerty': 60,
      'asdf_23': 350,
      'muthu-kumar': 's'
      }
print(d3)

for key, value in d3.items():
    if key == 'asdf_23':
        print("Key: {}, Value: {}".format(key, value))
        split_key = key.split('_')
        print('split_key: ', split_key)
        temp_list = []
        for i in split_key:
            if i.isdecimal():
                temp_list.append(int(i))
            else:
                temp_list.append(i)
        print('split_key after int filter: ', temp_list)
        for k in temp_list:
            print("Check type: ", k, type(k))

# 3.1 Creating a Dictionary
# Creating a dictionary using curly braces
sports_player = {
    "Name": "Sachin Tendulkar",
    "Age": 48,
    "Sport": "Cricket"
}
print("Dictionary using curly braces:", sports_player)
# Creating a dictionary using the dict() function
student_info = dict(name="Alice", age=21, major="Computer Science")
print("Dictionary using dict():", student_info)

# 3.2 Accessing Dictionary Items
student_info = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}
# Accessing values using square brackets
name = student_info["name"]
print("Name:", name)
# Accessing values using the get() method
age = student_info.get("age")
print("Age:", age)

age1 = student_info.get("age1")
print("Age1:", age1)  # None

# Set default value as None
age2 = student_info.get("age2", None)
print("Age2:", age2)  # None

# Set default value as own value
age3 = student_info.get("age3", "30")
print("Age3:", age3)  # None

# Will not check that key is exists or not
# name1 = student_info["name1"]
# print("Name1:", name1)  # KeyError: 'name1'


# 3.3 Modifying Dictionary Items
student_info = {
    "name": "Alice",
    "age": 22,
    "major": "Computer Science",
    "graduation_year": {'1st year': 2023,
                        '2nd year': 2024}
}
# Modifying an existing key-value pair
student_info["age"] = 22
# Adding a new key-value pair
student_info["graduation_year"]['2nd year'] = 2025
print("The modified dictionary is:", student_info)

# 3.4 Removing Dictionary Items
student_info = {
    "name": "Alice",
    "age": 22,
    "major": "Computer Science",
    "graduation_year": 2023
}
# Removing an item using the del statement
del student_info["major"]
# Removing an item using the pop() method
graduation_year = student_info.pop("graduation_year")
print(student_info)

# 3.5 Iterating Through a Dictionary
student_info = {
    "name": "Alice",
    "age": 22,
    "major": "Computer Science",
    "graduation_year": 2023
}
# Iterating through keys
for key in student_info:
    print("Keys:", key, student_info[key])

for key in student_info.keys():
    print("Keys(.keys()):", key)

# Iterating through values
for value in student_info.values():
    print("Values:", value)

# Iterating through key-value pairs
for key, value in student_info.items():
    print("Key:Value:", key, value)

# Iterating without unpack
for key in student_info.items():
    print("Key:Value:", key)

# Dict clear
dict = {'Name': 'Zara', 'Age': 7}
print("Start Len : %d" % len(dict))
dict.clear()
print("End Len : %d" % len(dict))

# Dict copy
dictionary = {5: 'x', 15: 'y', 25: [7, 8, 9]}
print("The given dictionary is: ", dictionary)
# using copy() method to copy
d2 = dictionary.copy()
print("The new copied dictionary is: ", d2)
# Updating the elements in second dictionary
d2[15] = 2
# updating the items in the list
d2[25][1] = '98'
print("The updated dictionary is: ", d2)

# Dict fromkeys
seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq)
print("New Dictionary : %s" % str(dict))

# Dict Setdefault
# Creating a dictionary
dict = {'Name': 'Zara', 'Age': 7}
res = dict.setdefault('RollNo')
# printing the result
print("The value of the key is: ", res)

dict_1 = {'Universe' : {'Planet' : 'Earth'}}
print("The dictionary is: ",dict_1)
# using nested setdefault() method
result = dict_1.setdefault('Universe', {}).setdefault('Muthu')
print("The nested value obtained is: ", result, dict_1)

# Dict Update
dict_1 = {'Name': 'Rahul', 'Hobby':'Singing', 'RollNo':34}
# updating the existing key
res = dict_1.update({'RollNo':45})
print('The updated dictionary is: ',dict_1)


