# 1-how big the data set is=shape=>returns(rows,columns)
# 2-what are the columns in the data set=columns=>returns list of columns,and names of the columns
# 3-what are the data types of the columns=dtypes=>returns data types of the columns
import pandas as pd
data={
  "Name":["Alice","Bob","Charlie","David","Eva","Frank","Grace","Hannah","Ian","Jack"],
  "Age":[25,30,35,40,45,50,55,60,65,70],
  "Salary":[50000,60000,70000,80000,90000,100000,110000,120000,130000,140000],
  "Performance_score":[80,85,90,95,88,92,87,91,89,93]
}
df=pd.DataFrame(data)
print(f"Shape of the data frame: {df.shape}")
print(f"Columns in the data frame: {df.columns}")
print(f"Data types of the columns: {df.dtypes}")