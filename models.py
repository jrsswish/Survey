import numpy as np
import pandas as pd

with open('data.csv', 'r') as infile:
  df = pd.read_csv(infile)

X = df[['Age']]

age_mean = np.mean(X)

print(age_mean)