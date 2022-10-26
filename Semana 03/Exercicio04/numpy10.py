import numpy as np

x = np.array([1, 2])
print(x.dtype)

x = np.array([1.0, 2.0])
print(x.dtype)

x = np.array([1, 2], dtype=np.int64) 
print(x.dtype)

x = np.array([1, 2], dtype=np.float32) 
print(x.dtype)

a = np.array([1,2,3])
b = a 
b[0] = 42
print(a)

a = np.array([1,2,3])
b = a.copy() 
b[0] = 42
print(a)