import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("/Users/eminibrahimoglu/Documents/Projects/python/python-journal/matplotlib/users.csv")
print(df)
print(df.columns)

grey = df[df.Username == "grey07"]

#plt.hist(grey.Identifier)
#plt.show()


#-------------------------------



# x = np.array([1,2,3,4,5,6,7])

# a = ["Türkiye","USA","Germany","Korea","Japan"]

# y = x*2+5

# plt.bar(a,y)
# plt.xlabel("x")
# plt.ylabel("y")
# #plt.show()


#-------------------------------

df.plot(grid=True, alpha = 0.5, subplots=True)

plt.subplot(2,1,1)
plt.plot(grey.Username)
plt.subplot(2,1,2)
plt.subplot(grey.Last_name)

plt.show()