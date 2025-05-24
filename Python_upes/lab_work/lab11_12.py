#Ques 1.
import numpy as np
# a. Convert numbers =[1, 2.0, 3] to numpy array and convert all elements to string type
numbers = [1, 2.0, 3]
array_str = np.array(numbers, dtype=str)
print("a. String array:", array_str)

# b. Create a 2D array through list and set dtype as int32
array_2d = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
print("b. 2D int32 array:\n", array_2d)

# c. Find the rows and columns of the 2D array created in part b
rows, cols = array_2d.shape
print("c. Rows:", rows, "Columns:", cols)

# d. Print 10 random numbers between 1 and 100
random_nums = np.random.randint(1, 101, size=10)
print("d. 10 random numbers between 1 and 100:", random_nums)

"""#Ques 2.
# a) Get help on the add function
print("Q2 a) Help on add function:")
help(np.add)"""

# b) Test whether none of the elements of a given array is zero
arr = np.array([1, 2, 3, 0])
none_zero = np.all(arr)
print("Q2 b) None of the elements is zero:", none_zero)

# c) Test whether any of the elements of a given array is non-zero
any_non_zero = np.any(arr)
print("Q2 c) Any element is non-zero:", any_non_zero)

# d) Generate an array of 15 random numbers from a standard normal distribution
normal_array = np.random.randn(15)
print("Q2 d) 15 random numbers from standard normal distribution:\n", normal_array)

"""
#Experiment 15
# a. Read the above Excel file in Python.
import pandas as pd
import numpy as np
data = [
    ['GOOGL', 27.82, 87, 845, 'larry page'],
    ['WMT', 4.61, 484, 'n.a.', 'n.a.'],
    ['MSFT', -1, 85, 64, 'bill gates'],
    ['RIL', 'not available', 50, 1023, 'mukesh ambani'],
    ['TATA', 5.6, -1, 'n.a.', 'ratan tata']
]

# c. Include column names
columns = ['ticker', 'eps', 'revenue', 'price', 'people']
df = pd.DataFrame(data, columns=columns)

# d. Convert 'not available' and 'n.a.' to NaN
df.replace(['not available', 'n.a.'], np.nan, inplace=True)

# Convert numeric columns to proper dtype
df['eps'] = pd.to_numeric(df['eps'], errors='coerce')
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Convert negative revenue to NaN
df.loc[df['revenue'] < 0, 'revenue'] = np.nan

# b. Write this DataFrame to a new CSV file "new.csv"
df.to_csv("new.csv", index=False)

# e. Fill NAN values using a suitable approach, e.g., fill revenue with mean
df['revenue'].fillna(df['revenue'].mean(), inplace=True)

# f. Write a function to change n.a. value appearing in WMT to "Sam Walton"
def update_people_column(df):
    df.loc[df['ticker'] == 'WMT', 'people'] = 'Sam Walton'
    return df

df = update_people_column(df)

# Final output
print(df)
"""