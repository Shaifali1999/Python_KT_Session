# 1. Python - Enums ==> With Enum class

# importing enum
from enum import Enum


class Subjects(Enum):
    ENGLISH = 1
    MATHS = 2
    SCIENCE = 3
    SANSKRIT = 4


obj = Subjects.MATHS
print(type(obj), obj)

# 1.2 Enum with @unique decorator
from enum import Enum, unique


@unique
class Subjects(Enum):
    ENGLISH = 1
    MATHS = 2
    GEOGRAPHY = 3
    # SANSKRIT = 2 # ValueError: duplicate values found in <enum 'Subjects'>: SANSKRIT -> MATHS


obj = Subjects.MATHS
print(type(obj), obj)

# 1.3 Anonymous Enum

from enum import Enum

Subjects = Enum("Subjects", "ENGLISH MATHS SCIENCE SANSKRIT")
print(Subjects.ENGLISH)
print(Subjects.MATHS)
print(Subjects.SCIENCE)
print(Subjects.SANSKRIT)


# 2. Access the name(key) and value(value)
class Subjects(Enum):
    ENGLISH = "E"
    MATHS = "M"
    GEOGRAPHY = "G"
    SANSKRIT = "S"


obj = Subjects.SANSKRIT
print(type(obj))
print(obj.name)
print(obj.value)

# 4. Iterating through Enums
from enum import Enum


class Subjects(Enum):
    ENGLISH = "E"
    MATHS = "M"
    GEOGRAPHY = "G"
    SANSKRIT = "S"


for sub in Subjects:
    print(sub.name, sub.value)

# 1. Python - Multithreading
"""
Notice that the process does not exit until the non-daemon thread (t1) finishes, 
even if the daemon thread (t2) is still running. If there were only the daemon thread running, 
the process would exit immediately after the main thread finishes.

Output:
-------
Non-daemon thread started
Daemon thread started
Non-daemon thread finished
Main thread exiting
Daemon thread finished
"""

import threading
import time


def non_daemon_thread():
    print("Non-daemon thread started")
    time.sleep(2)
    print("Non-daemon thread finished")


def daemon_thread():
    print("Daemon thread started")
    time.sleep(2)
    print("Daemon thread finished")


# Create a non-daemon thread
t1 = threading.Thread(target=non_daemon_thread)
t1.daemon = False  # Set this as a non-daemon thread

# Create a daemon thread
t2 = threading.Thread(target=daemon_thread)
t2.daemon = True  # Set this as a daemon thread

# Start both threads
t1.start()
t2.start()

# Wait for the non-daemon thread to finish
t1.join()

print("Main thread exiting")
