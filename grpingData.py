import pandas as pd
data={
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 25],  
    "salary": [50000, 60000, 70000]

}
df=pd.DataFrame(data)
grouped=df.groupby("age")["salary"].mean()
print(grouped)