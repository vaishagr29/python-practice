# =========================================
# PART 1: CODING QUESTIONS (1–10)
# =========================================

# 1. Import math and print sqrt of 16
import math
print(math.sqrt(16))

# 2. Random integer 1 to 10
import random
print(random.randint(1, 10))

# 3. Current date and time
import datetime
print(datetime.datetime.now())

# 4. Create module mymodule (mymodule.py)
# def greet():
#     print("Hello from module")

# Import in another file
# import mymodule
# mymodule.greet()

# 5. NumPy array
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)

# 6. List files in current directory
import os
print(os.listdir())

# 7. Import only pi
from math import pi
print(pi)

# 8. Package example
# mypackage/
# ├── __init__.py
# ├── module1.py
# └── module2.py

# module1.py
# def func():
#     print("Hello from module1")

# module2.py
# from .module1 import func
# func()

# 9. Python version
import sys
print(sys.version)

# 10. Pandas DataFrame
import pandas as pd
df = pd.DataFrame({
    "A": [1,2,3],
    "B": [4,5,6]
})
print(df)


# =========================================
# PART 2: INTERVIEW QUESTIONS (2 LINES)
# =========================================

def interview_answers():

    # 1. Module is a single Python file, package is a collection of modules.
    #    Library is a collection of packages/modules providing functionality.
    pass

    # 2. Specific function can be imported using: from module import function.
    #    Example: from math import sqrt
    pass

    # 3. __init__.py marks a directory as a Python package.
    #    It can also contain initialization code for the package.
    pass

    # 4. External libraries are installed using pip command.
    #    Example: pip install numpy
    pass

    # 5. Standard library comes with Python installation.
    #    Third-party libraries are installed separately using pip.
    pass


# =========================================
# PART 3: OUTPUTS
# =========================================

# 1.
# Output:
# 120

# 2.
# Output:
# Random number between 1 and 3

# 3.
# Output:
# 3.14

# 4.
# Output:
# 2023

# 5.
# Output:
# Current working directory path