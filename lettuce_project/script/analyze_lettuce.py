# === 0. IMPORT LIBRARIES ===
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ===1. LOAD DATA ===
#latin1 are safe for files including especial symbols e.g. °C.
df = pd.read_csv("lettuce_data/lettuce_dataset_updated.csv", encoding='latin1')

# === 2. CLEAN & TRANSFORM DATA ===

##Celsius to Fahrenheit
df['temperature_F'] = df['Temperature (°C)'] * 9/5 + 32

## Days to Weeks
df['Growth_Weeks'] = df['Growth Days'] / 7

## Remove % sign from Humidity and convert to float
df['humidity_clean'] = df['Humidity (%)'].astype(str).str.replace('%', '').astype(float)

## Convert date to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# === 3. VIEW COLUMN NAMES & SUMMARY STATISTICS ===

#Convert column headers into a Python-readable list
print("\n Column Names:\n", df.columns.tolist())

#Quick look at what kind of data we're working at
print("\n Sample Rows:\n", df.head())

# Display summary statistics of the dataset (min, max, mean, etc.)
print("\n Summary Statistics:\n", df.describe())
print("\n Median Values:\n", df.median())

# === 4. SMART Question Analysis ===

## Specific: Is there a connection between humidity and temperature?
correlation = df['Temperature (°C)'].corr(df['humidity_clean'])
print(f"\n Specific: Correlation between temperature and humidity: {correlation:.2f}")

## Measurable: What is average growth over one week?
avg_growth = df['Growth Days'].mean()
print(f"\n Measurable: Average growth is {avg_growth:.1f} days, or {avg_growth/7:.1f} weeks")

## Action-Oriented: Does TDS impact growth?
tds_corr = df['TDS Value (ppm)'].corr(df['Growth Days'])
print(f"\n Action-Oriented: Correlation between TDS and Growth Days: {tds_corr:.2f}")

## Relevant: Which variables predict growth?
growth_corr = df.corr()['Growth Days'].sort_values(ascending=False)
print("\n Relevant: Top predictors of growth:")
print(growth_corr)

## Time-Bound: What date range is this dataset?
min_date = df['Date'].min()
max_date = df['Date'].max()
print(f"\n Time-Bound: Dataset covers from {min_date.date()} to {max_date.date()}")

# === 5. VISUALIZE: Correlation Heatmap with Notes ===

# === Generate Heatmap ===
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap - Lettuce Dataset", fontsize=16)

# === Correlation Guide Box ===
guide_text = (
    "**Correlation Guide**\n"
    "• 1.00 = Perfect Positive Correlation\n"
    "• 0.00 = No Correlation\n"
    "• -1.00 = Perfect Negative Correlation"
)

# Create a textbox using fig.text and bbox

plt.gcf().text(
    0.5, 0.1,  # Position the text box below the plot  
    guide_text,
    ha='center',
    fontsize=12,
    bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5')
)

plt.subplots_adjust(bottom=0.4)  # Adjust space for the text box
plt.savefig("lettuce_data/lettuce_heatmap.png", bbox_inches='tight')
plt.show()

# === 6. SAVE THE CLEANED DATA ===
df.to_csv("lettuce_data/lettuce_cleaned.csv", index=False)
print("\n✅ Cleaned dataset saved as 'lettuce_cleaned.csv'")