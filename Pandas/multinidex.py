import numpy as np
import pandas as pd
from numpy.random import randn

outerIndex = ["Gruop1","Group1","Group1","Group2","Group2","Group2","Group3","Group3","Group3"]
innerIndex = ["Index1","Index1","Index1","Index2","Index2","Index2","Index3","Index3","Index3"]

hierarchy = list(zip(outerIndex,innerIndex))

hierarchy = pd.MultiIndex.from_tuples(hierarchy)

print(hierarchy)


df = pd.DataFrame(randn(9,3),hierarchy, columns = ["Column1","Column2","Column3"])
print(df)

##df.loc["Group1"]

#cf.xs("Index1",level="Indexes")