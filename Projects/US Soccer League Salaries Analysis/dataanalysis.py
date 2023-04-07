import numpy as np
import pandas as pd

df = pd.read_csv("../python-journal/Projects/US Soccer League Salaries Analysis/mls-salaries-2017.csv")
print(df)


print(len(df.index))


print(df.base_salary.mean()) # ortalama
print(df.base_salary.max()) # en yüksek maas
print(df.guaranteed_compensation.max()) # en yüksek tazminat
print(df[df["guaranteed_compensation"].max() == df["guaranteed_compensation"]]["last_name"]) # en yüksek tazminat


print(df[df["last_name"] == "Gonzalez Pirez"]["position"].iloc[0])


print(df.groupby("position").mean())



print(df["position"].nunique())

print(df["position"].value_counts())

print(df["club"].value_counts())


def son(last_name):
    if "son" in last_name.lower():
        return True
    return False

print(df[df["last_name"].apply(son)])