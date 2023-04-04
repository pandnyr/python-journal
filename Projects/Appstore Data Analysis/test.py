import pandas as pd

data = pd.read_csv('../python-journal/Projects/Appstore Data Analysis/archive/AppleStore.csv')

#data.info()
# Data columns (total 17 columns):
#  #   Column            Non-Null Count  Dtype  
# ---  ------            --------------  -----  
#  0   Unnamed: 0        7197 non-null   int64  
#  1   id                7197 non-null   int64  
#  2   track_name        7197 non-null   object **************
#  3   size_bytes        7197 non-null   int64  
#  4   currency          7197 non-null   object 
#  5   price             7197 non-null   float64
#  6   rating_count_tot  7197 non-null   int64  
#  7   rating_count_ver  7197 non-null   int64  
#  8   user_rating       7197 non-null   float64***************
#  9   user_rating_ver   7197 non-null   float64
#  10  ver               7197 non-null   object 
#  11  cont_rating       7197 non-null   object 
#  12  prime_genre       7197 non-null   object 
#  13  sup_devices.num   7197 non-null   int64  
#  14  ipadSc_urls.num   7197 non-null   int64  
#  15  lang.num          7197 non-null   int64  
#  16  vpp_lic           7197 non-null   int64  

# for idx in data.track_name:
#     print(idx)
for i in data.prime_genre:
    print(i)

print(data[["id", "user_rating", "prime_genre"]].describe())

id = data.id
rating = data.user_rating
genre = data.prime_genre
names = data.track_name

cleandata = pd.concat([id, names, rating, genre], axis=1)
print(cleandata)


