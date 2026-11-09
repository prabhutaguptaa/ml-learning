# it converts multi dim array into 1 dim array
# .ravel()->change oringinal array
# .flatten()->create copy of original array
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
b = a.ravel()
print(b)
print(a)

c = a.flatten()
print(a)

print(c)
