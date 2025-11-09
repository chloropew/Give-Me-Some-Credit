import pandas as pd

# Load the dataset (replace 'GiveMeSomeCredit.csv' with your actual file name)
data = pd.read_csv('GiveMeSomeCredit.csv')

# Show the first few rows of the dataset
print(data.head())

# Check for missing values in each column
print(data.isnull().sum())

data.isnull().sum()