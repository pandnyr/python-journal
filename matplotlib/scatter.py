import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/eminibrahimoglu/Documents/Projects/python/python-journal/matplotlib/users.csv")
print(df)
print(df.columns)

grey = df[df.Username == "grey07"]
plt.scatter(grey.Last_name, grey.First_name, color = "red", label = "grey")
plt.legend()
plt.xlabel("test")
plt.title("scatter plot")
plt.show()