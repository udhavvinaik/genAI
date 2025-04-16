'''
interpolate()
predicts missing data and then fills

1.preserve data integrity
2.smooth trends
3.avoid data loss

linear,polynomial,time

'''

import pandas as pd
data = {
    "Name":["ram","sham","geeta","seeta","raj"],
    "Age":[89,None,30,45,56],
    "Salary":[867569,None,30000,45000,500006],
    "Score":[809,None,350,45,506]
}

df = pd.DataFrame(data)
print(df)
df.interpolate(method="linear",axis=0,inplace=True)
print(df)

'''
used for:
1.time series data eg - stocks
2.numeric data with trend
'''


