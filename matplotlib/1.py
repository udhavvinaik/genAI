import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x_val = np.array([0,6])
y_val = np.array([3,10])

#plt.plot(x_val,y_val) #uses line by default
#if x_values are not provided to plot function it assumes them like 0,1,2,3,4,
#using marker instead of line
plt.plot(x_val,y_val,'o')
plt.show()