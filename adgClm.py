import pandas as pd
data={
  "name":["Alice","Bob","Charlie","David","Eva","Frank","Grace","Hannah","Ian","Jack"],
  "age":[25,30,35,40,45,50,55,60,65,70],
  "salary":[50000,60000,70000,80000,90000,100000,110000,120000,130000,140000],
  "city":["New York","Los Angeles","Chicago","Houston","Phoenix","Philadelphia","San Francisco","Seattle","Boston","Washington"]
  }
df=pd.DataFrame(data)
# adding column at last position
df["Bonus"]=df["salary"] * 0.1
print(df.head())
#  adding column at specific position
df.insert(2,"employment_id",["E001","E002","E003","E004","E005","E006","E007","E008","E009","E010"])
print(df.head())
