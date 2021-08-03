import numpy as np

# Assess Arrays

arr = np.array([(1,2,3), (4,5,6)])

print(arr)

print(arr.size)

print(arr.shape)

print(arr.ndim)

print(arr.dtype.name)

print(type(arr))

print(arr.itemsize)

# Creating Arrays

arr0 = np.array([1.1,2.2,3.3,4.4], dtype=complex)
print(arr0)

arr1 = np.arange(24)
print(arr1)

arr2 = np.arange(12, 24)
print(arr2)

arr3 = np.arange(12, 24, 2)
print(arr3)

arr4 = arr1.reshape(2, 3, 4)
print(arr4)

arr5 = np.zeros((6,7), dtype=np.int64)
print(arr5)

# Basic Operations

x = np.arange(12,24)
y = np.arange(0,24, 2)

print(x)
print("\n"*2)
print(y)

print(x-y)
print("\n"*2)
print(x*y)

print(x+10)
print("\n"*2)
print(y>10)
print("\n"*2)
print(y**3)

print(x.max())
print("\n"*2)
print(x.min())
print("\n"*2)
print(x.sum())

print(np.sqrt(x))

temp1 = np.arange(24).reshape(4,6)
temp2 = np.arange(24,48).reshape(6,4)

print(temp1)
print(temp2)
print(""*3)
# print(temp.sum(axis=1))
# print(temp.max(axis=0))
# print(temp.min(axis=1))

# print(temp1*temp2)
print(temp1@temp2)

temp3 = np.random.default_rng(3)

temp4 = temp3.random((6,4))

print(temp4*8)

# Thank you!
