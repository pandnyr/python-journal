import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_csv("/Users/eminibrahimoglu/Documents/Projects/python/python-journal/matplotlib/users.csv")
print(df)
print(df.columns)

df1 = df.drop(["Username"],axis=1)

print(df1)


#df1.plot()
#plt.show()

grey = df[df.Username.unique() == ["grey07"]] #usernamesi grey07 olanları ayırıp grey'e eşitledim
print("grey :",grey)

plt.plot(grey.Username ,grey.Last_name, color = "red", label = "greyxd")
plt.xlabel("A")
plt.ylabel("ez game")
plt.legend()
plt.show()

df1.plot(grid=True, linestyle = ":", alpha = 0.5) # alpha saydamlık ayarı
plt.show()

