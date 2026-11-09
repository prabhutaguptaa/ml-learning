""""
df["column name"].mean()  # it returns the mean of the column
df["colomn name"].median()  # it returns the median of the column
df["column name"].mode()  # it returns the mode of the column
df["column name"].sum()  # it returns the sum of the column
df["column name"].std()  # it returns the standard deviation of the column

"""
import pandas as pd
data={
  "name":["Alice",None,"Charlie","David","Eva","Frank","Grace","Hannah","Ian","Jack"],
  "age":[25,30,35,40,None,50,55,60,
65,70],
  "salary":[50000,60000,70000,80000,90000,None,110000,120000,130000,140000]
}
df=pd.DataFrame(data)
print(df["age"].mean())