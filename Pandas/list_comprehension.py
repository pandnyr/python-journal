import pandas as pd

dictx = {
        "NAME":["ALI","VELI","KENAN","HILAL","AYSE","NISA"],
        "AGE":[12,35,21,41,23,22],
        "MAAS":[100,124,356,984,234,567]
        }

dataFrame1 = pd.DataFrame(dictx)
print(dataFrame1)

ortalama_maas = dataFrame1.MAAS.mean()
print(ortalama_maas)


dataFrame1["maas_seviyesi"]  = ["dusuk" if ortalama_maas > each else "yuksek" for each in dataFrame1.MAAS ]

for each in dataFrame1.MAAS:
    if(ortalama_maas > each):
        print("dusuk")
    else:
        print("yuksek")

print(dataFrame1)

dataFrame1.columns = [each.lower() for each in dataFrame1.columns]

dataFrame1.columns = [each.split()[0]+"_"+each.split()[1] if len(each.split()>1) else each for each in dataFrame1.columns]