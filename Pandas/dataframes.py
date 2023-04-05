import numpy as np
import pandas as pd
from numpy.random import randn

array = randn(3,3)
print(array)


df = pd.DataFrame(data = randn(3,3), index = ["A","B","C"], columns = ["Column1","Column2","Column3"])
df.info()
print(df)

df["Column1"] # column1 values

type(df["Column2"])

df.loc["A"] # sort of index

df[["Column1","Column3"]]

df["Column4"] = pd.Series(randn(3),["A","B","C"])



df["Sum"] = df["Column1"] + df["Column2"] + df["Column3"] + df["Column4"]
print(df)


df.drop("Column4", axis=1, inplace=True) # axis belirtilmeli, inplace değeri değiştirilmediği sürece dataframe üzerinde değişmez.
print(df)

df.iloc[0] 
df.loc["A"]

df.loc["A","Column1"]
df.loc["B","Column2"]

df.loc[["A","B"],["Column1","Column2"]]

