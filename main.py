import pandas as pd

df = pd.read_csv("data/raw/OnlineNewsPopularity/OnlineNewsPopularity.csv")

print(df.shape)

print(df.columns)

print(df.info())

print(df.describe())