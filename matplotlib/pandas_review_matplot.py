import pandas as pd

df = pd.read_csv("/Users/eminibrahimoglu/Documents/Projects/python/python-journal/matplotlib/users.csv")
print(df)
print(df.columns)

print(df.Username.unique()) #tüm türleri yazdırıyor

print(df.info())

print(df.describe())

grey = df[df.Username.unique() == ["grey07"]] #usernamesi grey07 olanları ayırıp grey'e eşitledim
print("grey :",grey)
