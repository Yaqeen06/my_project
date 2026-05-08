#Full Exploratory Data Analysis (EDA)
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


sns.set_style('whitegrid')
df=pd.read_csv("data/raw/OnlineNewsPopularity/OnlineNewsPopularity.csv")

print("Data Shape",df.shape)
df.head()