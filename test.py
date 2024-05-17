import pandas as pd
from pandas-profiling import ProfileReport as Pr
import numpy as np

df1 = pd.read_csv("List of Countries by Sugarcane Production.csv")

print(df1)

profile = Pr(df1)

print(profile)