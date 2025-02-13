# ===================== Python Array =====================
import array as arr

# creating an array with integer type
a = arr.array('i', [1, 2, 3, ])
# a = arr.array('i', [1, 2, 3, 'qwerty']) # TypeError: 'str' object cannot be interpreted as an integer
print(type(a), a)

# creating an array with char type
a = arr.array('u', 'BAT')
print(type(a), a)

# creating an array with float type
a = arr.array('d', [1.1, 2.2, 3.3])
print(type(a), a)

# import array module
import array as arr

# open file object for writing
f = open('my_file.txt', 'wb')
# write array of integers to file object
arr1 = arr.array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Array in the file :", arr1)
arr1.tofile(f)
# close file
f.close()
# open file for reading
f = open('my_file.txt', 'rb')
# initialize array with integer type
array_one = arr.array("i")
# initialize array with integer type
array_two = arr.array("i")
# read 3 items from file
array_one.fromfile(f, 3)
print("Appended array1 :", array_one)
# Moving the cursor to the first position
f.seek(0)
# read 6 items from file
array_two.fromfile(f, 6)
print("Appended array2 :", array_two)
# close file
f.close()

import array as arr

arr3 = arr.array('d', [19.6, 24.9, 54.8, 60.8, 49.50])
print("Array Elements Before Appending :", arr3)
y = 'abcdefgi'
print(y.encode(), type(y.encode()))
arr3.frombytes(y.encode())
print("Array Elements After Appending :", arr3)

# =====================  File handling =====================
# Opening a file in read mode
file = open("example.txt", "r")
print(file.read())
file.close()
# Opening a file in write mode
file1 = open("example.txt", "w")
file1.write('abc')
file1.close()
# Opening a file in append mode
file2 = open("example.txt", "a")
file2.write('qwerty')
file2.close()
# Opening a file in binary read mode
file3 = open("example.txt", "ab")
file3.write(b'12\n')  # io.UnsupportedOperation: write
file3.write(b'qwedasd\nasdf\n')
file3.write(b'gfgfghfgdhg\n54y66666666666\n6666666666465346t5')
print("Name of the file: ", file3.name)
print("Closed or not: ", file3.closed)
print("Opening mode: ", file3.mode)
file3.close()
print("Closed or not:2 ", file3.closed)

# Reading a File in Python
"""
read() − Reads the entire file.
readline() − Reads one line at a time.
readlines() − Reads all lines into a list.
"""

# 1. read()
with open("example.txt", "r") as file:
    content = file.read()
    print('From read(): ', content)

# 2. readline()
with open("example.txt", "r") as file:
    line = file.readline()
    print('From readline(): ', line)

# 3. readlines()
with open("example.txt", "r") as file:
    lines_list = file.readlines()
    print('From readlines(): ', lines_list)
for i in lines_list:
    print(i)

# 4. read() with seek
with open("example.txt", "r") as file:
    file.seek(30, 0)
    content = file.read()
    print('From read(): ', content)

# Python Rename and Remove
import os
import time
import shutil

source_file = "example.txt"
dst_file = "example_1.txt"
print("Before copying file: {}".format(os.listdir(os.getcwd())))
dest = shutil.copyfile(source_file, dst_file)

list_of_files = os.listdir(os.getcwd())
print("After copying file: {}".format(list_of_files))

# Validate the file copy status
file_copy_sts = False
for each_file in list_of_files:
    if dst_file == each_file:
        print("For loop==> Successfully copied the file '{}' from this source file '{}'".format(dst_file, source_file))
        file_copy_sts = True

if file_copy_sts is False:
    print("Failed to copy file!")

# Alternative way to check file copy status
if dst_file in list_of_files:
    print("Alt if cond==> Successfully copied the file '{}' from this source file '{}'".format(dst_file, source_file))
else:
    print("Failed to copy file!")

# Current file name
current_name = "example_1.txt"
# New file name
new_name = "newfile.txt"
# Rename the file
os.rename(current_name, new_name)
print(f"File '{current_name}' renamed to '{new_name}' successfully.")
time.sleep(5)
os.rename(new_name, current_name)

# File to be deleted
file_to_delete = "example_1.txt"
# Delete the file
os.remove(file_to_delete)
print(f"File '{file_to_delete}' deleted successfully.")

# Directories in Python
# Checking if a Directory Exists
"""
os.path.exists()

Relative path − A path relative to the current working directory.
Absolute path − A complete path starting from the root directory.
# https://stackoverflow.com/questions/13819496/what-is-the-difference-between-makedirs-and-mkdir-of-os
"""

# 1. Python os.path.exists
directory_path = os.getcwd()
if os.path.exists(directory_path):
    print(f"The directory '{directory_path}' exists.")
else:
    print(f"The directory '{directory_path}' does not exist.")

# 2. Python makedirs and mkdir
new_directory = "new_dir"
nested_new_directory = "new_dir\dir_a\dir_b"
try:
    os.makedirs(nested_new_directory, exist_ok=True)
    print(f"makedirs ==> Directory '{nested_new_directory}' created successfully.")
except OSError as e:
    print(f"makedirs ==> Error: Failed to create directory '{nested_new_directory}'. {e}")

try:
    os.mkdir(new_directory)
    print(f"mkdir ==> Directory '{new_directory}' created successfully.")
except OSError as e:
    print(f"mkdir ==> Error: Failed to create directory '{new_directory}'. {e}")

# 3. Python chdir
cwd = os.getcwd()
print(f"Current working directory before change: {cwd}")
change_new_directory = r"%s" % cwd + '\\' + 'new_dir\\dir_a\\dir_b'
try:
    os.chdir(change_new_directory)
    print(f"Current working directory changed to '{change_new_directory}'.")
    cwd_after = os.getcwd()
    print(f"After==> Current working directory before change: {cwd_after}")
except OSError as e:
    print(f"Error: Failed to change working directory to '{change_new_directory}'. {e}")

# 4. Removing a Directory
"""
os.rmdir(directory_path)
# or
shutil.rmtree(directory_path)
"""
# Clean up for previous logic
os.chdir(cwd)
directory_path = change_new_directory

try:
    os.rmdir(directory_path)
    print(f"Directory '{directory_path}' successfully removed.")
except OSError as e:
    print(f"Error: Failed to remove directory '{directory_path}'. {e}")

# Open a file
# fo = open("example.txt", "r")
fo = open("C:\\Users\\muthukus\\Documents\\Python_scripts\\Python_KT\\new_dir\\test.py", "r")
print("Name of the file: ", fo.name)
file_contents = fo.read()

# Return the file descriptor
fid = fo.fileno()
# Display the file descriptor
print(f"FID: {fid}")
fo.flush()
print("Contents of the file: ", file_contents)
# Close opened file
fo.close()

# Python OS.Popen
import os
# Using popen() to execute the 'ls' command
fileStream = os.popen("dir")
res = fileStream.read()
print(res)

import os, sys

# Open a file
fd = os.open("example.txt", os.O_RDWR)

#getting file size
f_size = os.path.getsize("example.txt")

# Reading text
ret = os.read(fd, f_size)
print(f"Reading text from file: {f_size}, {ret}")

# Close opened file
os.close(fd)
print ("file closed successfully!!")

import os
for root, dirs, files in os.walk(".", topdown=True):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))
"""
False
.\new_dir\test.py
.\new_dir\dir_a
.\example.txt
.\kt03_func.py
.\kt04_module.py
.\kt05_module_execute.py
.\kt_01_and_02.py
.\kt_06_scope.py
.\kt_07_session.py
.\kt_08_session.py
.\kt_09_session.py
.\my_file.txt
.\new_dir

True
.\example.txt
.\kt03_func.py
.\kt04_module.py
.\kt05_module_execute.py
.\kt_01_and_02.py
.\kt_06_scope.py
.\kt_07_session.py
.\kt_08_session.py
.\kt_09_session.py
.\my_file.txt
.\new_dir
.\new_dir\test.py
.\new_dir\dir_a
"""

