# 1. Function example
import time

def func_05():
    print("")
    return 200, True, 'abc'

return_val, sec_val, thir_val = func_05()
print("return_val-1: ", return_val, sec_val, thir_val)

return_val = func_05()
print("return_val-2: ", return_val, type(return_val))
print("return_val-3: ", return_val[0], return_val[1], return_val[2])

# 2. Import example with as
import re as MuthuRegx
if MuthuRegx.search(r'^M.*R$', 'Muthu'):
    print("Match")
else:
    print("Not match")

# 3. Import without as
import re
if re.search(r'^M.*R$', 'Muthu'):
    print("Match")
else:
    print("Not match")

# 4.Import particular function(s)
from re import search, match, fullmatch
# 4.1 OR import all
from re import *  # try this also
if search(r'^M.*u$', 'Muthu'):
    print("Match")
else:
    print("Not match")

# 5. Membership Operators - in, not in
list_1 = [1, 'd', 'qwerty', 30]
if 'd' in list_1 and 2 not in list_1:
    print("Yes it is there")
else:
    print("Not there")
m = 'abc'
k = 'abc'

# 6. Identity Operators - is , is not
if m is k:
    print("match", id(m), id(k))
else:
    print("not match", id(m), id(k))

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = a

# 6.1 Comparing and printing return values
print(a is c)
print(a is b)

# Printing IDs of a, b, and c
print("id(a) : ", id(a))
print("id(b) : ", id(b))
print("id(c) : ", id(c))

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = a

# 6.2 Comparing and printing return values
print(a is not c)
print(a is not b)

# Printing IDs of a, b, and c
print("id(a) : ", id(a))
print("id(b) : ", id(b))
print("id(c) : ", id(c))

# 7. For raise example, and pass
if 'muthu' in list_1:
    print("Yes it is there")
else:
    print("Not there")
    # raise Exception("Sriram custom Exception - Not Found Error")
    pass

# 8. Try except finally
# x = 10
try:
    # x/0
    print("Display the X-value", x)
except:
    print("Something went wrong")
finally:
    # print("The 'try except' is finished")
    print("Script execution is completed")

# 9. yield example
def myFunc():
    # line 1
    # line 2
    # return 20
    yield "Hello"
    yield 51
    yield "Good Bye"


x = myFunc()
print("X value: ", x)
for z in x:
    print(z)
    time.sleep(1)
    print("End iteration")


a = 10
b = 'muthu'
c = [1, 4]

# 10. Casting
print(a, type(a))  # 10 <class 'int'>
a = str(a)
print(a, type(a))  # 10 <class 'str'>

# 11. Unicode
var = "\u00BE"
print (var)


# 12. How to convert string into a list
for j in range(5):
    print("Int:", j)

new_str_list = 'sri_ram-01'
print("hardcoded: ", new_str_list[0])

for each_ind in new_str_list:
    print("EACH: ", each_ind)

final_list = []
print("len of str: ", len(new_str_list))
for k in range(len(new_str_list)):
    print("Dynamic str:", new_str_list[k])
    final_list.append(new_str_list[k])
print(final_list)


# 13. Slice for string
# skip 3 numbers and print the number 1 to 8
#  1(start index), 2(skip), 3(skip), 4(print), 5(skip), 6(skip), 7(print), 8(exclude), 9   ==>>> positive order
# output: [1, 4, 7]
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("skip 3 numbers: ", l1[0:8:3]) # n-1=2
# 0th index ,end 8th ==> # n-1=2
for i in range(1, 8, 3):
  print(i)

# 14. Logical Operators
# Logical operators work with boolean values and are used in conditional statements.
x = True
y = False

# Logical AND
print(x and y)  # Output: False

# Logical OR
print(x or y)   # Output: True

# Logical NOT
print(not x)    # Output: False

# 15. Bitwise Operators
# Bitwise operators work with binary representations of integers and are used for low-level operations like bit manipulation.
a = 10  # Binary: 1010
b = 4   # Binary: 0100

# Bitwise AND
print(a & b)  # Output: 0 (Binary: 0000)

# Bitwise OR
print(a | b)  # Output: 14 (Binary: 1110)

# Bitwise XOR
print(a ^ b)  # Output: 14 (Binary: 1110)

# Bitwise NOT
print(~a)     # Output: -11 (Binary: ...11110101, two's complement)

# Bitwise left shift
print(a << 2) # Output: 40 (Binary: 101000)

# Bitwise right shift
print(a >> 2) # Output: 2 (Binary: 0010)

# ==============