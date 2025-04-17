import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

y_points = np.array([10,20,45,70])
#plt.plot(y_points,marker='o')
#if marker is not written only points are shown not line
#plt.show()

#format strings "fmt" - marker[line]colour
#colon -> dotted line
#r -> red
'''
line references
- solid
: dotted
--dashed
-. dashdot
'''

'''
colour references
r red
g green 
b blue
k black
w white
'''

#ms for marker size
#mec marker edge colour  can be putted with hash values
#mfc marker face colour
#linestyle for line type
#colour for colour
#linewidht for width
plt.plot(y_points,'*-r',ms=20,mec='k')
plt.show()

