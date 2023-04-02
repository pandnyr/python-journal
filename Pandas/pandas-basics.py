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
print(dataFrame1["MAAS"])


