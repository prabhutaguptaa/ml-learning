import pandas as pd


df=pd.read_json(r"Pandas\sample_Data.json",encoding='latin1')
print('displaying the info of the data frame')
print(df.info())