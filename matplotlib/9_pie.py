import numpy as np
import matplotlib.pyplot as plt

mtlabels = ["apple","mango","banana","cherry","papaya"]
#makes the portion come out
myexplode = [0.2,0,0,0,0] 
#shadow parameter shadow=true
#colours can also be passed as list


y = np.random.normal(170,50,5)
plt.pie(y,labels=mtlabels,explode=myexplode,shadow=True)
plt.legend(title="fruits") #shows description

plt.show()