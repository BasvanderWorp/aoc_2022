import numpy as np

# string input
a = np.matrix('1 2; 3 4')
print("Via string input : \n", a, "\n\n")

a2 = np.array('1 2; 3 4')

# array-like input
b = np.matrix([[5, 6, 7], [4, 6]])
print("Via array-like input : \n", b)