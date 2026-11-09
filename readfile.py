import pandas as pd

# df = pd.read_json("C:\\Users\\Prabhuta Gupta\\OneDrive\\Desktop\\ML\\Pandas\\sample_Data.json")
df=pd.read_json(r"Pandas\sample_Data.json",encoding='latin1')
print(df)
