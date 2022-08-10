import numpy as np
x = np.array([3, 5, 1, 2, 3])
y = np.array([2, 3, 3, 2, 1])
print("Array A")
print(x)
print("\nArray B")
print(y)
print("\nA>B")
print(np.greater(x,y))
print("\nA>=B")
print(np.greater_equal(x, y))
print("\nA<B")
print(np.less(x, y))
print("\nA<=B")
print(np.less_equal(x, y))



Array A
[3 5 1 2 3]

Array B
[2 3 3 2 1]

A>B
[ True  True False False  True]

A>=B
[ True  True False  True  True]

A<B
[False False  True False False]

A<=B
[False False  True  True False]
