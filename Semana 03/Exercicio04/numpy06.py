import numpy as np

a = np.array([[1,2], [3,4]])

print(a)

b = a[0,1]
print(b)

a = np.array([[1,2, 3,4], [3,4,5,6]])

b=a[0,:]
print(b)
b=a[0,1:3]
print(b)
b=a[:,1]
print(b)
b=a[-1,-1]
print(b)
b=a[-1,-2]
print(b)

a = np.array([[1,2], [3,4], [5,6]])
print(a)

bool_idx = a>2
print(bool_idx)
print(a[bool_idx])
print(a[a > 2])
b= np.where(a>2, a, -1)
print(b)

a = np.array([[10, 19, 30, 40, 45, 70]])
print(a)
b = [1, 3, 5]
print(a[b])
even = np.argwhere(a%2==0).flatten()
print(a[even])

