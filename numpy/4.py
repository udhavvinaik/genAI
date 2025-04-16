import numpy as np
arr1 = np.array([10,20,30,40,50,60,70,80])
arr2 = arr1.reshape(2,4)

#two methods to flat ravel() and flatten()
#ravel -> modifies orignal array
#flatten -> creates new copy
arr3 = arr2.flatten()
print(arr1)
print(arr2)
print(arr3)

#modifications
#insert(array,index,value,axis) Orignal remains unchanged
#axis is for 2D arrays
print("-------------------------")
print(arr1)
arr2 = np.insert(arr1,1,788)
print(arr2)

'''
concatenate method
concatenate((arr1,arr2),axis)
axis for 2d array
'''

'''
removal
np.delete(arr,index,axis) orignal is unchanged
'''

'''
spliting into sub
np.split(arr,no of parts)
value error if not sufficient elements
'''


