#df.sort_values(by="coloumn",True/False for order,inplace)
import pandas as pd
data={
    "Name":["arun","varun","tarun"],
    "Age":[12,564,9],
    "Salary":[123465,5673,987652]
}
df=pd.DataFrame(data)
print(df)
df.sort_values(by="Age",ascending=True,inplace=True)
print(df)
df.sort_values(by="Salary",ascending=False,inplace=True)
print(df)

print("----------------")
df.sort_values(by=["Age","Salary"],ascending=[True,False],inplace=True)
print(df)


#aggregation

data={
    "Name":["arun","varun","tarun","garun","narun"],
    "Age":[12,564,9,34,12],
    "Salary":[123465,5673,987652,123453,100000]
}
df=pd.DataFrame(data)
grouped = df.groupby("Age")["Salary"].sum()
print(grouped)

grouped = df.groupby(["Age","Name"])["Salary"].sum()
print(grouped)