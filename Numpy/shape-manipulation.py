import numpy as np

array = np.array([[1,2,3],[4,5,6],[7,8,9]])

a = array.ravel()

array2 = a.reshape(3,3)
arrayT = array2.T

print(array)
print(array2)
print(arrayT)

print(arrayT.shape)

array5 = np.array([[1,2,3],[4,5,6],[7,8,9]])

