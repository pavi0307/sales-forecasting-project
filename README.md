# Sales Forecasting Project

A Python project that predicts future retail sales using historical data with ARIMA time series forecasting.

## Table of Contents
- [About](#about)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Evaluation](#evaluation)
- [Business Insights](#business-insights)
- [License](#license)

## About
This project uses retail sales data (daily sales, inventory, and price) to build a time series forecasting model using ARIMA. The goal is to predict future sales trends to assist better inventory management and marketing decision-making.

## Installation
Make sure you have Python installed (version 3.6 or higher).  
Install the required packages using:


## Usage
1. Place your sales CSV file (`mock_kaggle.csv`) in the `data/` folder.  
2. Run the preprocessing script to load and clean the data:
3. Run the ARIMA forecasting model script:



This will output sales data visualization, model details, error metrics, and sales forecasts.

## Features
- Loads and preprocesses sales data  
- Explores sales trends with visualizations  
- Builds a time series sales forecasting model with ARIMA  
- Evaluates model using MSE, MAE, and R-squared metrics  
- Predicts and visualizes future sales trends  

## Evaluation
The ARIMA model's performance is measured with Mean Squared Error (MSE), Mean Absolute Error (MAE), and R-squared metrics to quantify prediction accuracy.

## Business Insights
The forecast helps businesses optimize inventory and marketing strategies by forecasting sales trends with historical data patterns. This reduces risks of overstock or shortages.

## License
This project is licensed under the MIT License. You are free to use, modify, and share it with attribution.


