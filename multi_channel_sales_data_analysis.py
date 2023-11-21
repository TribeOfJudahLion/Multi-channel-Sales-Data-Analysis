import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter, AutoDateLocator

# Load the extended sample data specifying the date format
data = pd.read_csv('sales_data_extended_sample.csv', parse_dates=['Date'], date_parser=lambda x: pd.to_datetime(x, format='%Y-%m-%d'))

# Set 'Date' as the index
data.set_index('Date', inplace=True)

# Resample the data by month and sum the sales
monthly_data = data.resample('M').sum()

# Calculate total sales for each channel
monthly_data['Total_Sales'] = monthly_data['Online_Sales'] + monthly_data['InStore_Sales'] + monthly_data['Direct_Sales']

# Creating a figure with three subplots
plt.figure(figsize=(15, 15))

# First plot - Total Monthly Sales
plt.subplot(3, 1, 1)
ax1 = plt.gca()
monthly_data['Total_Sales'].plot(kind='bar', ax=ax1)
ax1.set_title('Total Monthly Sales')
ax1.set_xlabel('Month')
ax1.set_ylabel('Total Sales')
formatted_dates = [date.strftime('%b %Y') for date in monthly_data.index]
ax1.set_xticklabels(formatted_dates, rotation=45, ha='right')

# Second plot - Sales Breakdown by Channel
plt.subplot(3, 1, 2)
ax2 = plt.gca()
monthly_data[['Online_Sales', 'InStore_Sales', 'Direct_Sales']].plot(kind='bar', stacked=True, ax=ax2)
ax2.set_title('Monthly Sales Breakdown by Channel')
ax2.set_xlabel('Month')
ax2.set_ylabel('Sales')
ax2.set_xticklabels(formatted_dates, rotation=45, ha='right')

# Third plot - Heatmap of Sales by Channel and Month
plt.subplot(3, 1, 3)
heatmap_data = monthly_data[['Online_Sales', 'InStore_Sales', 'Direct_Sales']]
sns.heatmap(data=heatmap_data.T, cmap='viridis', annot=True, fmt='.0f')
plt.title('Heatmap of Sales by Channel and Month')
plt.xlabel('Month')
plt.ylabel('Sales Channel')
plt.xticks(ticks=np.arange(0.5, len(formatted_dates)), labels=formatted_dates, rotation=45, ha='right')

# Improve layout to prevent overlap of subplot labels/titles
plt.tight_layout()

# Show the plot
plt.show()
