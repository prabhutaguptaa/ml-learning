import pandas as pd
data={
  "name":["Alice","Bob","Charlie","David","Eva","Frank","Grace","Hannah","Ian","Jack"],
  "age":[25,30,35,40,45,50,55,60,65,70],
  "salary":[50000,60000,70000,80000,90000,100000,110000,120000,130000,140000],
  "city":["New York","Los Angeles","Chicago","Houston","Phoenix","Philadelphia","San Francisco","Seattle","Boston","Washington"]
  }
df=pd.DataFrame(data)
# inplace=True will make changes in the original dataframe
df.drop(columns=['city'], inplace=True)
print(df.head())
df.drop(columns=['city', 'salary'], inplace=True)
print(df.head())
