# Task 42 - Pandas installation / getting started
# Installation (run in a terminal):  pip install pandas
#                      or with conda: conda install pandas
import sys
import pandas as pd
import numpy as np

print("Python:", sys.version.split()[0])
print("pandas:", pd.__version__)
print("numpy :", np.__version__)

# Check that pandas works
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
print("Installation OK" if len(myvar) == 3 else "Something is wrong")
print("\nUseful options:")
pd.set_option("display.max_columns", 10)
print("display.max_columns =", pd.get_option("display.max_columns"))
