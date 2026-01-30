# ==============================
# TASK 2: UNEMPLOYMENT ANALYSIS
# ==============================

# Step 1: Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load the dataset
df = pd.read_csv("Unemployment in India.csv")

# Step 3: Display basic information
print("First 5 rows of dataset:")
print(df.head())

print("\nDataset Shape:", df.shape)
print("\nColumn Names:")
print(df.columns)

# Step 4: Data Cleaning
df.columns = df.columns.str.strip()     # Remove extra spaces
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
 # Convert Date column

print("\nMissing Values:")
print(df.isnull().sum())

# Step 5: Basic Statistics
print("\nUnemployment Rate Statistics:")
print(df['Estimated Unemployment Rate (%)'].describe())

# Step 6: Overall unemployment trend
plt.figure(figsize=(10,5))
sns.lineplot(
    x='Date',
    y='Estimated Unemployment Rate (%)',
    data=df
)
plt.title("Unemployment Rate Trend in India")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 7: Covid-19 Impact Analysis
covid_start = "2020-03-01"

before_covid = df[df['Date'] < covid_start]
during_covid = df[df['Date'] >= covid_start]

print("\nAverage Unemployment Before Covid:",
      before_covid['Estimated Unemployment Rate (%)'].mean())

print("Average Unemployment During Covid:",
      during_covid['Estimated Unemployment Rate (%)'].mean())

plt.figure(figsize=(10,5))
sns.lineplot(
    x='Date',
    y='Estimated Unemployment Rate (%)',
    data=before_covid,
    label="Before Covid"
)
sns.lineplot(
    x='Date',
    y='Estimated Unemployment Rate (%)',
    data=during_covid,
    label="During Covid"
)
plt.title("Impact of Covid-19 on Unemployment")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 8: Rural vs Urban Analysis
plt.figure(figsize=(8,5))
sns.boxplot(
    x='Area',
    y='Estimated Unemployment Rate (%)',
    data=df
)
plt.title("Urban vs Rural Unemployment Rate")
plt.show()

# Step 9: Seasonal Trend Analysis
df['Month'] = df['Date'].dt.month

plt.figure(figsize=(8,5))
sns.barplot(
    x='Month',
    y='Estimated Unemployment Rate (%)',
    data=df
)
plt.title("Monthly Average Unemployment Rate")
plt.show()

# Step 10: State-wise Unemployment
state_avg = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean()

print("\nAverage Unemployment Rate by State:")
print(state_avg.sort_values(ascending=False))

print("\n--- Analysis Completed Successfully ---")
