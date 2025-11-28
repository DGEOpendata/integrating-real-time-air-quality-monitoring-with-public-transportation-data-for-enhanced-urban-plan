python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
transport_data = pd.read_csv('public_transport_usage.csv')
air_quality_data = pd.read_csv('real_time_air_quality.csv')

# Data preprocessing
# Assume both datasets have a 'date' column and a 'location' column
transport_data['date'] = pd.to_datetime(transport_data['date'])
air_quality_data['date'] = pd.to_datetime(air_quality_data['date'])

# Merge datasets on date and location
merged_data = pd.merge(transport_data, air_quality_data, on=['date', 'location'])

# Analysis: Correlate transport usage with air quality indicators
correlation_matrix = merged_data.corr()
print('Correlation Matrix:', correlation_matrix)

# Visualize data
plt.figure(figsize=(10, 6))
sns.lineplot(data=merged_data, x='date', y='transport_usage', label='Transport Usage')
sns.lineplot(data=merged_data, x='date', y='PM2.5', label='PM2.5 Levels')
plt.title('Public Transport Usage vs PM2.5 Levels')
plt.xlabel('Date')
plt.ylabel('Values')
plt.legend()
plt.show()

# Identify high pollution and high usage areas
high_pollution_usage = merged_data[(merged_data['PM2.5'] > 50) & (merged_data['transport_usage'] > 1000)]
print('High Pollution and Usage Areas:', high_pollution_usage[['location', 'date', 'PM2.5', 'transport_usage']])
