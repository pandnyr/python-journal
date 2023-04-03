import pandas as pd

dictx = {
        "NAME":["ALI","VELI","KENAN","HILAL","AYSE","NISA"],
        "AGE":[12,35,21,41,23,22],
        "MAAS":[100,124,356,984,234,567]
        }

dataFrame1 = pd.DataFrame(dictx)
print(dataFrame1)


print(dataFrame1.drop(["MAAS"],axis=1,inplace= True))

data1 = dataFrame1.head()
data2 = dataFrame1.tail()

data_concat = pd.concat([data1,data2],axis=0) #vertical
print(data_concat)


maas = dataFrame1.maas
age = dataFrame1.age

datahorizontal = pd.concat([maas,age],axis=1) #horizontal
print(datahorizontal)