import pandas as pd
data={
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35]
}
df = pd.DataFrame(data)
df.to_json("output.json", index=False)