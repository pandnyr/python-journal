import numpy as np

array = np.array([1,2,3,4,5,6,7])

print(array[0])

print(array[0:4])

reverse_array = array[::-1]
print(reverse_array)


array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array1[1,1])

print(array1[:,1])

print(array1[1,1:4])

print(array1[:,-1])