import pandas as pd
data={
  "name":["Alice","Koca","Charlie","David","Eva","Frank","Grace","Hannah","Ian","Jack"],
  "age":[25,30,35,40,None,50,55,60,65,70],
  "salary":[50000,60000,70000,80000,90000,None,110000,120000,130000,140000],
  
  }
df=pd.DataFrame(data)

# linear interpolation,polynomial interpolation, spline interpolation,time interpolation,nearest neighbor interpolation,zero order hold interpolation,forward fill interpolation,backward fill interpolation

# df.interpolate(method='linear')

numeric_cols = df.select_dtypes(include='number').columns

df[numeric_cols] = df[numeric_cols].interpolate(method='linear')

print(df)