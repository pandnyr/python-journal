import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9]) # 1*9 vector
print(array.shape)

a = array.reshape(3, 3)
print("shape : ",a.shape)
print("dimension : ", a.ndim)
print("data type : ", a.dtype.name)
print("size : ", a.size)
print("type : ",type(a))
print(a)

array1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(array1)


zeros = np.zeros((3,4))
zeros[0,0] = 5
print(zeros)

np.ones((3,4))

np.empty((3,4))

a = np.arange(10,50,5)
print(a)

a = np.linspace(10,50,20)
print(a)


#------------------------------------------


