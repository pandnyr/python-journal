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
print(df[df["views"].min() == df["views"]]["title"].iloc[0])

print(df.groupby("category_id").mean()["comment_count"])

print(df["category_id"].value_counts())


def countTitleCount(title):
    return len(title)
df["title_length"] = df["title"].apply(countTitleCount)


def countTag(tags):
    tagList = tags.split("|")
    return len(tagList)
df["tag_count"] = df["tags"].apply(countTag)