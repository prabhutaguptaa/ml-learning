import pandas as pd
data={
  "name":["Alice",None,"Charlie","David","Eva","Frank","Grace","Hannah","Ian","Jack"],
  "age":[25,30,35,40,None,50,55,60,65,70],
  "salary":[50000,60000,70000,80000,90000,None,110000,120000,130000,140000],
  "city":["New York","Los Angeles","Chicago","Houston","Phoenix","Philadelphia","San Francisco","Seattle","Boston","Washington"]
  }
df=pd.DataFrame(data)
# df.dropna(inplace=True)
# print(df)
# df.fillna(0,inplace=True)
# print(df)
df["age"].fillna(df["age"].mean(),inplace=True)
df["salary"].fillna(df["salary"].mean(),inplace=True)
df["name"].fillna("Unknown",inplace=True)
print(df)