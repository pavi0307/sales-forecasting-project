import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, r2_score

# Load and prepare data
data = pd.read_csv('../data/mock_kaggle.csv')
data['data'] = pd.to_datetime(data['data'])
data = data.sort_values('data').set_index('data')

# Fit ARIMA model: order (2,1,2) is an example, tune as needed
model = ARIMA(data['venda'], order=(2, 1, 2))
model_fit = model.fit()

# Summary of model
print(model_fit.summary())

# Forecast next 30 days after the dataset
forecast = model_fit.forecast(steps=30)

# Prepare actual last 30 days for evaluation (if available)
y_true = data['venda'][-30:]
y_pred = forecast[:len(y_true)]  # Align length with actual data

# Calculate and print error metrics
mae = mean_absolute_error(y_true, y_pred)
r2 = r2_score(y_true, y_pred)

print(f"Mean Absolute Error (MAE): {mae}")
print(f"R-squared: {r2}")

# Plot historical sales and forecast
plt.figure(figsize=(12, 6))
plt.plot(data['venda'], label='Historical Sales')
plt.plot(forecast.index, forecast, color='red', label='Forecasted Sales')
plt.title('Sales Forecast using ARIMA')
plt.legend()
plt.show()
