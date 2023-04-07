import numpy as np
import pandas as pd

dataset = {
    "Departman" : ["Bilişim","İK","Üretim","Üretim","Bilişim","İK"],
    "Çalışan" : ["Mustafa","Jale","Kadir","Zeynep","Murat","Ahmet"],
    "Maaş" : [3000,3500,2500,4500,4000,2000]
}

df = pd.DataFrame(dataset)

print(df)

DepGroup = df.groupby("Departman")
print(DepGroup)

print(DepGroup.sum()) # toplam departmanlarda ki toplam maaşlar
df.groupby("Departman").sum().loc["Bilişim"] # bilişimde ki toplam maaşlar

df.groupby("Departman").count() # her bir departmanda ki toplam çalışan sayısı

print(df.groupby("Departman").max())


df.groupby("Departman").min()


df.groupby("Departman").min()["Maaş"]["Bilişim"]


df.groupby("Departman").mean()["Maaş"]["İK"] # maaşların ortalaması




