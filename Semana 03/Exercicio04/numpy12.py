import numpy as np

print(np.random.random((3,2)))

print(np.random.randn(3,2))

R = np.random.randn(10000)
print(R.mean(), R.var(), R.std())

R = np.random.randn(10, 3)
print(R.mean())

print(np.random.randint(3,10,size=(3,3)))

print(np.random.choice(7, size=10))

print(np.random.choice([1,2,3,4], size=8))