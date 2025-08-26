import pandas as pd

# Load CSV file from the data folder
data = pd.read_csv('../data/mock_kaggle.csv')

# Show first 5 rows of data
print("First 5 rows:\n", data.head())

# Summary information about data
print("\nData Info:")
print(data.info())

# Basic statistics of numerical columns
print("\nStatistical Summary:")
print(data.describe())
