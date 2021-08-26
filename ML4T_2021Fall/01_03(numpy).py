""" Creating NumPy Array"""

from util import *
import numpy as np
import random as rand
#print(get_file_path("SPY.csv"))

#print(np.array([(1,2,3), (3,4,5)]))
#print(np.random.random((2,2)))
#print(np.random.normal(size = (2,2)))
na = np.random.randint(0 , 10, (5,5))
print(na)
print(na.sum(axis=1), na.max(axis=0), na.min())
na.sum()