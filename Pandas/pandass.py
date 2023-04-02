# hızlı ve etkili for dataframes
# csv ve text dosyalarını açıp inceleyip sonucları bu dosya tiplerine cevirebiliriz.


import pandas as pd

dictx = {"NAME":["ALİ","VELİ","KENAN","HİLAL","AYSE","NİSA"],
        "AGE":[12,35,21,41,23,22],
        "MAAŞ":[100,124,356,984,234,567]}

dataFrame1 = pd.DataFrame(dictx)
print(dataFrame1)

head = dataFrame1.head()
tail = dataFrame1.tail()