import pandas as pd

df = pd.DataFrame({"column1": [True, False,True]})

print(df)

df["column1"].replace({'True': "x", 'False': "y"}, inplace=True)

print(df)