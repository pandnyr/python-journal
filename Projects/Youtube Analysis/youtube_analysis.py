import pandas as pd 

df = pd.read_csv("../python-journal/Projects/Youtube Analysis/USvideos.csv")

print(df)

print(df.head(5))

df.drop(["thumbnail_link","video_id","trending_date","publish_time","thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed"],axis = 1,inplace = True)
print(df) 

print(len(df.columns))


print(df["likes"].mean())
print(df["dislikes"].mean())

print(df[df["views"].max() == df["views"]]["title"].iloc[0])

