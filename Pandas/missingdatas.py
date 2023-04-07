import numpy as np
import pandas as pd

arr = np.array([[10,20,np.nan],[5,np.nan,np.nan],[21,np.nan,10]])

print(arr)


df = pd.DataFrame(arr,index = ["Index1","Index2","Index3"],columns=["Column1","Column2","Column3"])

print(df)

print(df.dropna(axis = 1))

print(df.dropna(thresh = 2)) #min 2 nan yoksa silmez


print(df.fillna(value = 1)) # nan yerine ne geleceğini belirler


df.sum().sum()

print("df size : ",df.size)

df.isnull().sum() # nan olanları döner

def calculateMean(df):
    totalSum = df.sum().sum()
    totalNum = df.size - df.isnull().sum().sum()
    return totalSum / totalNum


df.fillna(value = calculateMean(df), inplace=True)


