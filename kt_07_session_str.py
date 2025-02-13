# String
str = "hello world"
print(str[0])
# str[0]='i' # TypeError: 'str' object does not support item assignment
print(str)

# String with multi-line
str2= """Welcome To TutorialsPoint
hello world"""
print(str2)

# String slice
var1 = 'Hello World!'
print ("Updated String :- ", var1[:6] + 'Python')
str1 = "hello"
str2 = "world"
print("a" in str1)
print(str1 * 3)
print(str1.capitalize())

# String Formatting Operator
print ("My name is %s and weight is %d kg!" % ('Zara', 21))
name = "John"
age = 30
print("Name: {}, Age: {}".format(1, 100))
print("Name: {}, Age: ".format(1, 200))
print("Name: {}, Age: ".format(1, 300))
# print("Name: {}, Age: {}".format(1)) # IndexError: Replacement index 1 out of range for positional args tuple
print("Name: {}, Age: ".format(1))
print("Name: , Age: ".format(1, 400))
print("Name: {}, Age: {}".format(1, 500, 'Z'))
print("{}".format(1, 800))
print("**{} {}**".format(1, 'P'))
print("{}{} {}".format(1, 900, 'a'))


# String count
str = "Hello! Welcome to Tutorialspoint.";
substr = "i";
print("The number of occurrences of the substring in the input string are: ", str.count(substr, 3, 30))

# String endswith
str = "Hello!Welcome to Tutorialspoint.py";
suffix = ".py";
result=str.endswith(suffix)
print("The input string ends with the given suffix:", result)

# String find
str1 = "Hello! Welcome to Tutorialspoint."
str2 = " "
result= str1.find(str2, 12, 15)
result= str1.find(str2)
print("The index where the substring is found:", result)

# String format_map
person = {'name': 'Alice', 'age': 25, 'xyz': 20}
# Name and Age
result = "Name: {name}, Age: {age}".format_map(person)
print(result)

# Unknown key used format_map
# result = "Name: {name}, {abc}".format_map(person)  # KeyError: 'abc'
# print(result)

# Name and xyz
result = "Name: {name}, {xyz}".format_map(person)
print(result)

# Format with Dict key access
result = "Name: {}, Age: {}".format(person['name'], person['age'])
print(result)

# String with index
str1 = "Hello! Welcome to Tutorialspoint."
str2 = "to"
result= str1.index(str2, 5)
p = len(str1)-5
print("Len:", p)
print(str1.index('We', 0, p))
print("The index where the substring is found:", result)
result= str1.index(str2, 18)
print("The index where the substring is found:", result)

# String isidentifier
identifier = "my_variable1%$6"
result = identifier.isidentifier()
print("The result is:",result)

# 'is' means, validating the given string, retrun Boolean(True, False)
str = "Hello!welcome"
result=str.isalpha()
print("Are all the characters of the string alphabetic?", result)

# String maketrans and translate
mydict = {'m': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5'}
str = "Welcome to Tutorialspoint muthu"
print("Translation Table: ")
print(str.maketrans(mydict))
print(type(str.maketrans(mydict)))

# using trantab on translate() function
print(str.translate(str.maketrans(mydict)))

intab = "aeiou"
outtab = "12345"
# mydict = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
str = "this is string example....wow!!!"
trantab = str.maketrans(intab, outtab)
print("Translation Table: ")
print(trantab)
print()

# using trantab on translate() function
print(str.translate(trantab))

# String lstrip
str = "8888asdf8888this is string example....wow!!!8888888";
print(str.lstrip('8'))

str = '  Welcome to Tutorialspoint     '
print("##{}##".format(str.lstrip(' ')))
print("##{}##".format(str.rstrip(' ')))
print("##{}##".format(str.strip(' ')))

# String join
seq_tuple = ["m", "u", "t", 'h', "u"] # This is sequence of strings.
ret = "@".join(seq_tuple)  # TypeError: sequence item 0: expected str instance, int found
print("Ret: %s" % ret)

# String join alternative method
temp_list = []
con_str = ''
for i in seq_tuple:
    print("each index: ", i)
    temp_list.append(i)
    con_str += i

print("Temp list: {}, \t used Join method: {}".format(temp_list, ''.join(temp_list)))
print("Conc: ", con_str)

# String partition
text = "apple banana orange"
result = text.partition(' ')
print(result)

# String split
str1 = "abcde, 12345, !@#$%";
str2 = "14<65<189<235<456"
print(str1.split(','))
print()
print(str2.split('<'))

# String splitlines
str1 = "Names:\nAlex\nJohn\x1cRichard\nNick"
print("String before splitting: " + str1)
print("String after splitting:")
print(str1.splitlines())

# String zfill
str = "Welcome to Tutorialspoint"
print(len(str))
print(str.zfill(26))

# String sort of str
list1 = ["2","3","7","1","8","2","10","11","15","21","20","18"]
list1.sort()
print(list1)
a = id(1)
b = id(1)
print(a,b)

c = 1
d = 1
print(id(c),id(d))

# String sort of int
list1 = [2,3,7,1,8,2,10,11,15,21,20,18]
list1.sort()
print(list1)

