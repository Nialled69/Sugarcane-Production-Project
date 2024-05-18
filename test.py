
# This is just a test file, It contributes nothing to the original project
# I just tested a few things and tried some module instances here for the overall working of the project
# Imagine opening this     XD     (couldn't be me)


import pandas as pd

from pandas-profiling import ProfileReport as Pr

import numpy as np

df1 = pd.read_csv("List of Countries by Sugarcane Production.csv")

print(df1)

# df1 = df1["Countries"].agg(np.mean)

profile = Pr(df1)

print(profile)

df_continent = df.groupby("Continents").sum()

print(df_continent)
