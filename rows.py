import pandas as pd

df=pd.read_json(r"Pandas\sample_Data.json",encoding='latin1')
print("starting 10 rows of the data frame")
print(df.head(10))
print("ending 5 rows of the data frame itself")
print(df.tail())