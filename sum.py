import numpy as np
x = np.array([[1,0],[0,1]])
print("Array")
print(x)
print("\nSum of all elements")
print(np.sum(x))
print("\nSum of each column")
print(np.sum(x, axis=0))
print("\nSum of each row")
print(np.sum(x, axis=1))






Sum of each column
[1 1]

Sum of each row
[1 1]

Process finished with exit code 0