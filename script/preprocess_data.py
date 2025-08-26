import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('../data/mock_kaggle.csv')

# Convert 'data' column to datetime format for easier time operations
data['data'] = pd.to_datetime(data['data'])

# Sort data by date (important for time series)
data = data.sort_values('data')

# Check for missing values
print("Missing values in each column:\n", data.isnull().sum())

# If there are missing values, drop or fill them (here we drop)
data = data.dropna()

# Plot sales (venda) over time to visualize trends
plt.figure(figsize=(12,6))
plt.plot(data['data'], data['venda'], label='Sales (venda)')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Over Time')
plt.legend()
plt.show()
