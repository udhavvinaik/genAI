import pandas as pd

data = {
    "Name":["ram","sham","geeta","seeta","raj"],
    "Age":[89,20,30,45,56],
    "Salary":[867569,289000,30000,45000,500006],
    "Score":[809,220,350,45,506]
}

df = pd.DataFrame(data)

#adding coloumns
df["Bonus"] = df["Salary"]*0.1
#print(df)

#df.insert(location,coloumn name,values)
df.insert(1,"Employee ID",[10,20,30,40,50])
print(df)

#updating values
#df.loc[row_index,coloumn name] = new value
df.loc[1,"Employee ID"]=100
print(df)

#df.drop(coloumns=["Column name"],inplace=True)
