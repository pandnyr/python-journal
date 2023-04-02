import numpy as np
array1 = np.array([[1,2],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]])

array3 = np.vstack((array1, array2)) # vertical

array4 = np.hstack((array1,array2)) # horizontal

print(array1)
print(array2)
print(array3)
print(array4)



#-------------------------------



liste = [1,2,3,4]

array = np.array(liste)

liste2 = list(array)

a = np.array([1,2,3])
b = a
b[0] = 5
c = a

d = np.array([1,2,3])

e = d.copy()
f = d.copy()