#adding labels
import matplotlib.pyplot as plt
import numpy as np

x = np.array([10,20,30,40,55,67])
y = np.array([2,34,45,67,89,90])
'''
plt.plot(x,y,marker='o',color='r')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title ("sample plot")
plt.show()
'''

#creating varibles/dictionary
font1 = {'family':'serif',"color":'blue',"size":20}
font2 = {'family':'serif',"color":'darkred',"size":15}

plt.plot(x,y)
plt.xlabel("x-axis",fontdict=font2)
plt.ylabel("y-axis",fontdict=font2)
plt.title ("sample plot",fontdict=font1)
plt.show()

#loc attribute for location left,centre,right