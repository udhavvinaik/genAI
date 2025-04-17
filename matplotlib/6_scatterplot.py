import matplotlib.pyplot as plt
import numpy as np

x = np.array([12,22,33,45,65,76,78,8,9,10,11,12])
y = np.array([2,62,3,45,5,71,74,80,99,3,3,5])
colours = np.array([10,20,30,40,50,60,70,80,90,100,110,120])
plt.scatter(x,y,c=colours,cmap='viridis')
plt.colorbar()


x = np.array([1, 4, 6, 7, 9, 11, 13, 15, 17, 19, 21, 23])
y = np.array([2, 3, 5, 8, 10, 12, 14, 16, 18, 20, 22, 24])
sizes = np.array([10,20,30,40,50,60,70,80,90,100,110,120])
plt.scatter(x,y,c=colours,cmap='winter',s=sizes,alpha=0.5)
#alpha for transparency
plt.colorbar()



plt.show()
