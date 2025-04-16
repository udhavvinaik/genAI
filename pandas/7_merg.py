import pandas as pd

#pd.merge(df1,df2,on="coloumn",how="type of join")

df_customers = pd.DataFrame({
    "cus_id":[1,2,3],
    "Name":["ramesh","suresh","resh"]
})

df_orders = pd.DataFrame({
    "cus_id":[1,2,4],
    "amt":[124,234,789]
})

merged = pd.merge(df_customers,df_orders,on="cus_id",how="outer")
print(merged)
print("-------------")

merged = pd.merge(df_customers,df_orders,on="cus_id",how="inner")
print(merged)

print("---------------------")
merged = pd.merge(df_customers,df_orders,how="cross")
print(merged)
