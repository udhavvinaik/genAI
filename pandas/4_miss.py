import pandas as pd
data = {
    "Name":["ram",None,"geeta","seeta","raj"],
    "Age":[89,None,30,45,56],
    "Salary":[867569,None,30000,45000,500006],
    "Score":[809,None,350,45,506]
}

df = pd.DataFrame(data)

print(df)
print(df.isnull())
#True if None  False if present

#counts missing values
print(df.isnull().sum())

'''
delete missing values
axis=0 for rows
axis=1 for coloumns

df.dropna(inplace=True)
print(df)
'''

#filling missing values
#df.fillna(0,inplace=True)
#print(df)

#using calculated values
df["Age"].fillna(df["Age"].mean(),inplace=True)
df["Salary"].fillna(df["Salary"].mean(),inplace=True)
print(df)