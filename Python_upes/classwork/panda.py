# DSA Series Examples
import pandas as pd
from numpy import array

# Create a Series from list
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

# Create a Series from ndarray without index value
data = array(['a', 'b', 'c'])
s = pd.Series(data)
print(s)

# Create a Series from ndarray with customized index values
data = array(['a', 'b', 'c', 'd', 'e'])
s = pd.Series(data, index=[100, 101, 102, 103, 104])
print(s)

# Create a Series from a dictionary
data = {'a': 0., 'b': 1., 'c': 2.}
s = pd.Series(data)
print(s)

# Create a Series from dictionary with custom index
s = pd.Series(data, index=['b', 'c', 'd', 'a'])
print(s)

# Create a Series from a scalar value
s = pd.Series(5, index=[0, 1, 2, 3])
print(s)

# DSA DataFrame Examples

# Create a DataFrame from dictionary
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df)

# Create a DataFrame with named index
df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df)

# Iterating over a DataFrame (rows)
for index, row in df.iterrows():
    print(index, row['calories'], row['duration'])