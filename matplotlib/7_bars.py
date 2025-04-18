#plotting bargraphs
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["a","b","c","d","e"])
y = np.array([3,7,8,10,11])
plt.bar(x,y,width=0.8)
#plt.barh(x,y) for plotting horizontal bargraph
#color for colour
#width for width
#for horizontal use height instead of width
plt.show()