import pandas as pd

dictx = {
        "NAME":["ALI","VELI","KENAN","HILAL","AYSE","NISA"],
        "AGE":[12,35,21,41,23,22],
        "MAAS":[100,124,356,984,234,567]
        }

dataFrame1 = pd.DataFrame(dictx)
print(dataFrame1)

print(dataFrame1.columns)
print(dataFrame1.info())
print(dataFrame1.dtypes)
print(dataFrame1.describe()) # numeric features = columns (age, maas)

print(dataFrame1["NAME"])
print(dataFrame1["AGE"])
print(dataFrame1.AGE)

print(dataFrame1["MAAS"])

dataFrame1["yeni feature"] = [-1,-2,-3,-4,-5,-6]

print(dataFrame1.loc[:, "AGE"])

print(dataFrame1.loc[:3,"AGE"])

print(dataFrame1.loc[:3, "AGE":"NAME"])

print(dataFrame1.loc[::-1,:])

print(dataFrame1.loc[:,:"NAME"])

print(dataFrame1.iloc[:,2])
