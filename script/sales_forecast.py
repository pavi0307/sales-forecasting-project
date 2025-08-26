import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('../data/mock_kaggle.csv')
data['data'] = pd.to_datetime(data['data'])
data = data.sort_values('data').reset_index(drop=True)

# Use the day number as a feature to predict sales
data['day_num'] = (data['data'] - data['data'].min()).dt.days

# Features and target
X = data[['day_num']]
y = data['venda']

# Split data (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict sales on test data
y_pred = model.predict(X_test)

# Calculate mean squared error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Plot actual vs predicted sales
plt.figure(figsize=(10,5))
plt.scatter(X_test, y_test, color='blue', label='Actual Sales')
plt.scatter(X_test, y_pred, color='red', label='Predicted Sales')
plt.xlabel('Day Number')
plt.ylabel('Sales')
plt.title('Actual vs Predicted Sales')
plt.legend()
plt.show()
