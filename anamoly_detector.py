import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Load Zillow Data
df = pd.read_csv("zillow_real_estate_data.csv")

# Print available columns to check for date-related fields
print("Columns in dataset:", df.columns)

# Identify the correct date column
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'])
    date_column = 'date'
elif 'lastSoldDate' in df.columns:
    df['lastSoldDate'] = pd.to_datetime(df['lastSoldDate'])
    date_column = 'lastSoldDate'
elif 'publishedDate' in df.columns:
    df['publishedDate'] = pd.to_datetime(df['publishedDate'])
    date_column = 'publishedDate'
else:
    print("❌ No valid date column found in dataset. Exiting...")
    exit()

# Ensure 'price' column exists
if 'price' in df.columns:
    # Train Isolation Forest Model for Anomaly Detection
    model = IsolationForest(contamination=0.05, random_state=42)
    df['anomaly'] = model.fit_predict(df[['price']])

    # Extract anomalies
    df_anomalies = df[df['anomaly'] == -1]

    # Plot anomalies
    plt.figure(figsize=(12,6))
    plt.scatter(df[date_column], df['price'], label='Normal Prices')
    plt.scatter(df_anomalies[date_column], df_anomalies['price'], color='red', label='Anomalies')
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

    print("✅ Anomaly detection completed!")
else:
    print("❌ Error: 'price' column not found in dataset.")

print(df.head(10))  # Show the first 10 rows
