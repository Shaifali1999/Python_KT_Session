# 1. Regex
# re.match(pattern, string, flags=0)
"""
. ==> Matches with any single character except newline '\n'.
? ==> match 0 or 1 occurrence of the pattern to its left
+ ==> 1 or more occurrences of the pattern to its left
* ==> 0 or more occurrences of the pattern to its left
"""
import re

# 1. re.match
line = "dogs Cats are smarter than dogs"
matchObj = re.match(r'(cats)|(dogs)', line, flags=re.I)
print(f"Object: {matchObj}")
if isinstance(matchObj.groups(), tuple):
    print(matchObj.start(), matchObj.end())
    print("IF ==> matchObj.group() : ", matchObj.group(1), matchObj.group(2))
else:
    print("Else ==> matchObj.group() : ", matchObj.group())

# 2. re.search
line = "dogs Cats are smarter than dogs"
matchObj = re.search(r'(cats)|(dogs)', line, flags=re.I)
print(matchObj.start(), matchObj.end())
print("matchObj.group() : ", matchObj.groups())

# 3. re.match vs re.search
line = "Cats are smarter than dogs"
matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

searchObj = re.search(r'dogs', line, re.M | re.I)
if searchObj:
    print("search --> searchObj.group() : ", searchObj.group())
else:
    print("Nothing found!!")

# 4. improving the re.match to find the entire line or specific word(s)
line = "Cats are smarter than dogs"
matchObj = re.match(r'.*are', line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

matchObj = re.match(r'.*are.*', line, re.M | re.I)
# print(f"Object: {matchObj}")
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

# 5. why r'' Raw string using in Regex (PEP 8: W605 invalid escape sequence '\w')
if re.match(r'\w+', line):
    print("matched")
else:
    print("not matched")

# 6. re.findall
string = "Simple is better than complex."
ret_op = re.findall(r"le", string)
if ret_op:
    print(f"Findall==> 1-Matched: {ret_op}")
else:
    print(f"Findall==> 1-Not-matched: {ret_op}")
ret_op = re.findall(r"abc", string)
if ret_op:
    print(f"Findall==> 2-Matched: {ret_op}")
else:
    print(f"Findall==> 2-Not-matched: {ret_op}")

# 6.1 re.findall-example-2
string = "Simple is better, than complex."
# string = '1234qwe3445asdf1\n'
findall_ret = re.findall(r"\w*", string)
# print(f"findall_ret: {findall_ret}, {type(findall_ret)}")
# if isinstance(findall_ret, list) or isinstance(findall_ret, tuple):
if findall_ret:
    for i in findall_ret:
        print(f"each line: {i}")
    else:
        print(f"Inside ELSE ==> findall_ret is Empty!: {findall_ret}")
else:
    print(f"FINAL ELSE==> findall_ret is Empty: {findall_ret}")

# 7. re.sub()
phone = "2004-959-559 # This is Phone Number"
# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
"""" REMOVE only from # to end of the line(a-zA-Z)
#  This is Phone Number
"""
print("Phone Num : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)  # \D == [^\d]  ==> REMOVE only the \d+(0-9)
print("Phone Num : ", num)

# 8. re.compile

string = "Simple is better than complex. Complex is better than complicated."
pattern = re.compile(r'is')
obj = pattern.match(string)
obj = pattern.search(string)
print(obj.start(), obj.end())

obj = pattern.findall(string)
print(obj)

obj = pattern.sub(r'was', string)
print(obj)

# 9. re.finditer
string = "Simple is better than complex. Complex is better than complicated."
pattern = re.compile(r'is')
iterator = pattern.finditer(string)
print(iterator)

for match in iterator:
    print(match.span())

"""
'Greedy' means match longest possible string.
    1. <.*> ==> Greedy repetition: matches "<python>perl>"
'Lazy' means match shortest possible string.
    2. <.*?> ==> Nongreedy: matches "<python>" in "<python>perl>"

Example:
test string : stackoverflow
greedy reg expression : s.*o output: [stackoverflo]w
lazy reg expression : s.*?o output: [stacko]verflow
"""
