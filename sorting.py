# sorting data
# sorting data 1colomn sort_values()
# df.sort_values(by="colomn name",ascending=True,inplace=True)  # it returns the sorted dataframe in ascending order  
import pandas as pd
data={
  "name":["Alice","Koca","Charlie","David","Eva","Frank","Grace","Hannah","Ian","Jack"],
  "age":[25,30,35,40,None,50,55,60,65,70],
  "salary":[50000,60000,70000,80000,90000,None,110000,120000,130000,140000],
  "city":["New York","Los Angeles","Chicago","Houston","Phoenix","Philadelphia","San Francisco","Seattle","Boston","Washington"]
  }
df=pd.DataFrame(data)
# df.sort_values(by="name",ascending=True,inplace=True)
df.sort_values(by=["age","salary"],ascending=[True,False],inplace=True  )
print(df)