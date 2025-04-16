import pandas as pd
df = pd.read_json("pandas\sample_Data.json",encoding="utf8")
#print(df)
#print("top 5 rows")
#print(df.head()) # parameter for specific number

#print("bottom 5 rows")
#print(df.tail())

'''
info() method
1.number of rows/coloumns
2.coloumn names
3.data types
4.non null count
5.memory usage
'''

#print(df.info())
#print(df.describe())


data = {
    "Name":['ram','sham','rrr','aaa'],
    "Age":[10,20,30,40],
    "Salary":[50000,230000,45000,344589],
    "Score":[500,400,450,344]
}

#df = pd.DataFrame(data)
#print(df)
#print(df.describe()) 

#print(df.shape)
#print(df.columns)

df = pd.DataFrame(data)
print(df)
name = df['Name']
print(name)

subset = df[['Name','Salary']]
print(subset)

high = df[df['Score'] > 420]
print(high)

filtered = df[(df['Score']>420) & (df['Age']>10)]
print(filtered)
