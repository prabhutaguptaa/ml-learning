import pandas as pd
data={
    "name": ["Alice", "Bob", "Charlie", "Bob"],
    "age": [25, 30, 25, 30],  
    "salary": [50000, 60000, 70000, 80000]

}
df=pd.DataFrame(data)
grouped=df.groupby(["age", "name"])["salary"].mean()
print(grouped)