import pandas as pd

OG_PATH = "og.csv"

df = pd.read_csv(OG_PATH)

print(df.columns[1:])
