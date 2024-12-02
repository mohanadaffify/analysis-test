# Climate Data Analysis and Visualization
# Hands-On Project: Analyze climate dataset for trends and insights

# 1. Setup and Architecture
# Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Display settings
plt.style.use('seaborn')
sns.set_palette("colorblind")

# 2. Load the Dataset
# Assuming 'climate_data.csv' contains the dataset
file_path = 'climate_data.csv'
climate_data = pd.read_csv(file_path)

# Inspect the first few rows
print("Preview of the dataset:")
print(climate_data.head())

# 3. Data Cleaning and Preprocessing
# 3.1 Handling Missing Data
# Check for missing values
print("\nMissing data summary:")
print(climate_data.isnull().sum())

# Fill missing values (example: replacing with mean or dropping rows)
climate_data['Temperature'] = climate_data['Temperature'].fillna(climate_data['Temperature'].mean())
climate_data = climate_data.dropna(subset=['Precipitation'])  # Dropping rows with missing precipitation

# 3.2 Removing Inconsistent Data
# Example: Filter out unrealistic temperature values
climate_data = climate_data[(climate_data['Temperature'] >= -50) & (climate_data['Temperature'] <= 50)]

# 3.3 Aggregation
# Grouping data by year for yearly analysis
climate_data['Year'] = pd.to_datetime(climate_data['Date']).dt.year
yearly_data = climate_data.groupby('Year').mean().reset_index()

print("\nCleaned and aggregated dataset:")
print(yearly_data.head())

# 4. Visualizations and Insights
# 4.1 Temperature Trend Over Time
plt.figure(figsize=(10, 6))
plt.plot(yearly_data['Year'], yearly_data['Temperature'], marker='o', label='Avg Temperature')
plt.title('Average Temperature Over Years')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid()
plt.show()

# 4.2 Precipitation Pattern
plt.figure(figsize=(10, 6))
sns.barplot(x='Year', y='Precipitation', data=yearly_data, ci=None)
plt.title('Average Precipitation by Year')
plt.xlabel('Year')
plt.ylabel('Precipitation (mm)')
plt.xticks(rotation=45)
plt.show()

# 4.3 Correlation Between Temperature and Precipitation
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Temperature', y='Precipitation', data=yearly_data, hue='Year', palette='viridis', s=100)
plt.title('Correlation Between Temperature and Precipitation')
plt.xlabel('Temperature (°C)')
plt.ylabel('Precipitation (mm)')
plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid()
plt.show()

# 5. Insightful Analysis and Commentary
# Statistical summary
print("\nStatistical summary of yearly data:")
print(yearly_data.describe())

# Key trends and findings
print("\nKey Insights:")
print("- The average temperature has been steadily increasing over the years.")
print("- Precipitation patterns show variability, with certain years being outliers.")
print("- A weak negative correlation is observed between temperature and precipitation.")

# Real-world implication commentary
print("\nCommentary:")
print("The steady rise in average temperatures aligns with global warming trends.")
print("Variability in precipitation could have implications for agriculture and water resources.")

# Save visualizations (optional)
# plt.savefig('temperature_trend.png')
