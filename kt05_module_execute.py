# I. Import filename
import kt04_module
# II. Import particular func/class from the filename
from kt04_module import myfunction
# III. Import all var/func/class
from kt04_module import *

# 1. Step-I(import kt04_module), Call function with filename
x = kt04_module.myfunction(5, 6)
print(x)

# 2. Call module and get return value
z = myfunction(2, 3)
print("Display returned value:", z)

# 3. Call module and without return value
myfunction(2, 3)

# 4. Check dir of module
print(dir(kt04_module))
return_val2 = myfunc_2(10, 5)

