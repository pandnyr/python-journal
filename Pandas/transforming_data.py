import pandas as pd


dictx = {
        "NAME":["ALI","VELI","KENAN","HILAL","AYSE","NISA"],
        "AGE":[12,35,21,41,23,22],
        "MAAS":[100,124,356,984,234,567]
        }

dataFrame1 = pd.DataFrame(dictx)
print(dataFrame1)


liste = dataFrame1["list_comp"] = [each*2 for each in dataFrame1.AGE]
print(liste)

#-------------------------

def multiply(AGE):
    return AGE*2

dataFrame1["apply_metodu"] = dataFrame1.AGE.apply(multiply)
print(dataFrame1)