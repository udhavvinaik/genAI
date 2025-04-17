import matplotlib.pyplot as plt
import numpy as np

#first
x = np.array([0,1,2,3])
y = np.array([3,5,7,8])
plt.subplot(2,3,1)
#it has 1 row, 2 coloumns and is 1st plot
plt.title("sales")
plt.plot(x,y)

#second
x= np.array([11,23,45,56])
y =np.array([1,2,3,5])
plt.subplot(2,3,2)
#it has 1 row, 2 coloumn and is 2nd plot
plt.title("sales")
plt.plot(x,y)

#third
x = np.array([0,1,2,3])
y = np.array([3,5,7,8])
plt.subplot(2,3,3)
#it has 1 row, 2 coloumns and is 1st plot
plt.title("sales")
plt.plot(x,y)

#fourth
x= np.array([11,23,45,56])
y =np.array([1,2,3,5])
plt.subplot(2,3,4)
#it has 1 row, 2 coloumn and is 2nd plot
plt.title("sales")
plt.plot(x,y)

#fifth
x = np.array([0,1,2,3])
y = np.array([3,5,7,8])
plt.subplot(2,3,5)
#it has 1 row, 2 coloumns and is 1st plot
plt.title("sales")
plt.plot(x,y)

#sixth
x= np.array([11,23,45,56])
y =np.array([1,2,3,5])
plt.subplot(2,3,6)
#it has 1 row, 2 coloumn and is 2nd plot
plt.title("sales")
plt.plot(x,y)


plt.suptitle("data analytics")
plt.show()