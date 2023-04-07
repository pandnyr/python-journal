import numpy as np
import pandas as pd

df = pd.DataFrame({
    "Column1" : [1,2,3,4,5,6],
    "Column2" : [100,100,200,300,300,100],
    "Column3" : ["Mustafa","Deva","Kamil","Emre","Ayşe","Zeynep"]
})
print(df)

df.head(n = 3) # n değeri kadarını döner

df["Column2"].unique()

df["Column2"].value_counts()

print(df[(df["Column1"] >= 4) & (df["Column2"] == 300)])


def times3(x):
    return x * 3


times3(6)


df["Column2"] = df["Column2"].apply(times3)
print(df)


lambda x : x * 2 # apply fonk içine de yazılabilir

df["Column2"].apply(lambda x : x * 2)


df.drop("Column1", axis = 1, inplace= True)

df.columns

len(df.index)

df.index.names

df.sort_values("Column2", ascending=False) # ascending küçükten büyüğe doğru sıralar false yaparsak tam tersi olur

