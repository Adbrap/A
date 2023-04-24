import numpy as np
import pandas as pd
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt





data = []

#data2 = [0, 1, 2, 3, 2, 3, 4, 5, 4, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 2, 3, 4, 5]
#data3 = [1.20, 1.24, 1.18, 1.13, 1.16, 1.20, 1.23, 1.14, 1.06, 1.11, 1.16, 1.21, 1.17, 1.14, 1.17, 1.20, 1.19]
data3 = [5000, 5015, 5018,5001,4980,5080,5035,5125,5100,5138,5154,5168]

for argument in data3:
    data.append(argument)

data1 = {'c': data}
df = pd.DataFrame(data=data1)

localmax = argrelextrema(df['c'].values, np.greater, order=1, mode="clip")[0]
localmin = argrelextrema(df['c'].values, np.less, order=1, mode="clip")[0]

highs = df.iloc[localmax, :]
low = df.iloc[localmin, :]


fig1 = plt.figure(figsize=(10,7))
plt.plot([], [], " ")
plt.title(f'IETE : SOLDE COMPTE', fontweight="bold", color='black')
df['c'].plot(color=['blue'])
plt.scatter(x=highs.index, y=highs["c"])
plt.scatter(x=low.index, y=low["c"])
plt.show()

