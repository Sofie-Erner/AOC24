import pandas as pd
import numpy as np

df = pd.read_csv('day1.csv',names=["L1","L2"],header=None,sep=r"\s+") # Read in CSV with column names L1 and L2

list1 = np.sort(df["L1"].to_numpy())
list2 = np.sort(df["L2"].to_numpy())

dist = [ abs(list1[i] - list2[i]) for i in range(len(list1)) ]

print(sum(dist))