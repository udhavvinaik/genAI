import numpy as np
arr_2d = np.array([[1,2,3],[4,5,6]])

print(arr_2d.shape) #dimentions of array

arr = np.array([1,2,3,4,5,6])
print(arr.size)  #number of elements

#ndim = number of dimensions
print(arr_2d.ndim)

#.dtype = data type of element
a = np.array(["h","ig","kjl"])
print(a.dtype)
print(arr.dtype)

#astype = change datatype
arr = np.array([1.2,4.5,6,4])
print(arr.dtype)
a = arr.astype(int)
print(a.dtype)