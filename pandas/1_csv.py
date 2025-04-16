import pandas as pd
df = pd.read_csv("pandas\Mall_Customers.csv",encoding="utf8")
#print(df)

df = pd.read_json("pandas\sample_Data.json")
#print(df)

data = {
    "Name":["abc","pqr","xyz"],
    "Age":[10,20,30],
    "City":["Haryana","punjab","up"]
}

df = pd.DataFrame(data)
print(df)

#to csv
#df.to_csv("outp.csv",index=False)

#to excel
#df.to_excel("outp.xlsx",index=False)

#to json
#df.to_json("outp.json",index=False)


