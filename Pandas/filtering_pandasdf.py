import pandas as pd
import numpy as np
from numpy.random import randn

dictx = {
        "NAME":["ALI","VELI","KENAN","HILAL","AYSE","NISA"],
        "AGE":[12,35,21,41,23,22],
        "MAAS":[100,124,356,984,234,567]
        }

dataFrame1 = pd.DataFrame(dictx)
print(dataFrame1)

filtre1 = dataFrame1.MAAS > 200
print(filtre1)

filtrelenmis_data = dataFrame1[filtre1] # maaşı 200ün üzerinde olanları filtreleyip kaydediyor
print(filtrelenmis_data)

filtre2 = dataFrame1.AGE < 20
print(filtre2)

filtrelenmis_data2 = dataFrame1[filtre2]
print(filtrelenmis_data2)


print(dataFrame1[filtre1 & filtre2]) # 2 filtreye göre sıraladım.


#--------------------------------------------------


df = pd.DataFrame(randn(4,3),["A","B","C","D"],["Column1","Column2","Column3"])
print(df)


booleanDf = df > 0
print(booleanDf)


print(df[booleanDf])

# df[df > 2] # filtrelenebilir

print(df[df["Column1"] > 0])