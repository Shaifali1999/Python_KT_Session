# =============== 1. Import local package Directory(mypackage) ==> Before Install Setup.py file  ===============
from mypackage.areafunctions import rectangle
from mypackage.mathsfunctions import average

print("Import local package Directory(mypackage) ==> Area :", rectangle(10, 20))
print("Import local package Directory(mypackage) ==> average:", average(10, 20))

# ==============================================================
# =============== 2. Install Setup.py ==========================
r"""
1. cd C:\Users\muthukus\Documents\Python_scripts\Python_KT\MakePackage
2. python setup.py install
3. ls
    Mode                 LastWriteTime         Length Name
    ----                 -------------         ------ ----
    d-----         12/4/2024   3:01 PM                build
    d-----         12/4/2024   3:01 PM                dist
    d-----         12/4/2024   2:45 PM                mypackage
    d-----         12/4/2024   3:01 PM                mypackage.egg-info
    -a----         12/4/2024   3:02 PM            560 run_script.py
    -a----         12/4/2024   2:56 PM            341 setup.py

4. Install setup.py file
(.venv) PS C:\Users\muthukus\Documents\Python_scripts\Python_KT\MakePackage> pip list
Package    Version
---------- -------
mypackage  1.0
pip        24.3.1
setuptools 68.2.0
wheel      0.41.2
"""

# =============== 3. Import Converted package(mypackage) directly ==> After Installed Setup.py ===============
# Example-1
from mypackage import mathsfunctions

ret_val_pwr = mathsfunctions.power(4, 2)
print(f"Import Converted package(mypackage) directly ==> ret_val_pwr: {ret_val_pwr}")

# Example-2
import mypackage as pc

ret_val = pc.mathsfunctions.average(5, 10)
print(f"Import Converted package(mypackage) directly ==> ret_val: {ret_val}")

# Example-3
import mypackage.areafunctions as ar
import mypackage.mathsfunctions as ma

ret_val_for_rec = ar.rectangle(5, 8)
ret_val_avg = ma.average(2, 6)

print(f"Import Converted package(mypackage) directly ==> ret_val_for_rec: {ret_val_for_rec}")
print(f"Import Converted package(mypackage) directly ==> ret_val_avg: {ret_val_avg}")
