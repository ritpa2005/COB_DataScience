import pandas as pd
import numpy as np

missing = ["Not Given", np.nan]
df = pd.read_csv("D:\COB_DataScience\dataset - netflix1.csv", na_values= missing)
print(df.isnull().sum())

df["country"].fillna(method = 'ffill', inplace = True)
df_sorted = df.sort_values("country")
df_sorted.fillna(method = 'ffill', inplace = True)

df_result = df_sorted.sort_index()

df_result.to_csv("result_dataset-netflix1.csv")
