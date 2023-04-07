import pandas as pd

dataset = pd.read_csv("../python-journal/Pandas/dataset reading/USvideos.csv")
print(dataset)

newdataset1 = dataset.drop(["video_id","trending_date"],axis = 1)
print(newdataset1)

newdataset1.to_csv("USvideosnew.csv", index=False)