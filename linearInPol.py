import pandas as pd
data={
  "age":[25,30,35,40,None,50,55,60,65,70],
  "salary":[50000,60000,70000,80000,90000,None,110000,120000,130000,140000]
}

df=pd.DataFrame(data)
# df.interpolate(method='linear',inplace=True)
# print(df)
df['age'] = df['age'].interpolate(method='linear')
print(df)
# 1.timer series data
# 2.numeric data with trend
# 3.avoid dropping rows with missing values