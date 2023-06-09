import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import os
import seaborn as sns

data = pd.read_csv('../python-journal/Projects/World Happines Report/archive/2016.csv')
data.info()
data.describe()
data.head()

data[data['Country'] == 'Canada']
data[data['Country'] == 'United States']

data['Region'].unique()
for region in data['Region'].unique():
    print(len(data[data['Region'] == region]), region)

rows_list = []

for region in data['Region'].unique():
    happinessRankSum = data.loc[data['Region'] == region]['Happiness Rank'].sum()
    numCountriesInRegion = len(data.loc[data['Region'] == region])
    avgHappinessScorePerRegion = happinessRankSum/numCountriesInRegion;
    dict1 = {'Region': region, 'Happiness Rank Per Region': avgHappinessScorePerRegion, 'numCountriesInRegion': numCountriesInRegion};
    rows_list.append(dict1)

df = pd.DataFrame(rows_list)
df.sort_values(['Happiness Rank Per Region'], ascending=True, inplace=True)


plt.figure(figsize=(10,10))
plt.bar(df['Region'], df['Happiness Rank Per Region'], align='center')
plt.xlabel("Regions")
plt.ylabel("Happines Score")
plt.show()


#------------------------

data2015 = pd.read_csv('../python-journal/Projects/World Happines Report/archive/2015.csv')
data2016 = pd.read_csv('../python-journal/Projects/World Happines Report/archive/2016.csv')
data2017 = pd.read_csv('../python-journal/Projects/World Happines Report/archive/2017.csv')
data2018 = pd.read_csv('../python-journal/Projects/World Happines Report/archive/2018.csv')
data2019 = pd.read_csv('../python-journal/Projects/World Happines Report/archive/2019.csv')

# rows = []

# for happines in data2015['Happines Score'].unique():
#     happinessRankSum = data2015.loc[data2015['Happines Score'] == happines]['Happiness Rank'].sum()
#     avgHappinessScorePerRegion = happinessRankSum/happines
#     dict1 = {'Happines Score': happines, 'Happiness Rank Per Region': avgHappinessScorePerRegion, 'numCountriesInRegion': numCountriesInRegion};
#     rows_list.append(dict1)

# print(rows)