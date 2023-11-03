import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_aggregated_data_with_best_fit(file_path):
    # Load data
    df = pd.read_csv(file_path, parse_dates=['# Date'])
    
    # Aggregate data by month
    monthly_data = df.resample('M', on='# Date').sum()

    # Fit a line of best fit (degree 1 polynomial)
    x = np.arange(len(monthly_data))
    y = monthly_data['Receipt_Count']
    coefficients = np.polyfit(x, y, 1)
    best_fit_line = np.polyval(coefficients, x)

    # Plot the aggregated data and line of best fit
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_data.index, y, marker='o', linestyle='-', label='Actual Data')
    plt.plot(monthly_data.index, best_fit_line, linestyle='--', color='red', label='Best Fit Line')
    plt.xlabel('Date')
    plt.ylabel('Receipt Count')
    plt.title('Monthly Aggregated Receipt Counts with Line of Best Fit')
    plt.legend()
    plt.grid(True)
    plt.savefig("aggregated_data_best_fit_plot.png")
    plt.show()

plot_aggregated_data_with_best_fit('data_daily.csv')
