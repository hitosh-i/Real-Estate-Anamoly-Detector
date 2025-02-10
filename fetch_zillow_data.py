import requests
import pandas as pd

# Zillow API URL (via RapidAPI)
url = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"

# Set your API Key from RapidAPI
headers = {
    "X-RapidAPI-Key": "0f8a7c6f9amsh0befe77e963dc24p1a2b98jsn5c696a62bfb3",  # Replace with your actual API Key
    "X-RapidAPI-Host": "zillow-com1.p.rapidapi.com"
}

# Define search parameters (modify location as needed)
querystring = {
    "location": "Georgia, GA",
    "status": "for_sale"
}

# Send API Request
response = requests.get(url, headers=headers, params=querystring)

# Check response status
if response.status_code == 200:
    data = response.json()

    # Ensure response contains property data
    if 'props' in data:
        df = pd.DataFrame(data['props'])

        # Save to CSV
        df.to_csv("zillow_real_estate_data.csv", index=False)
        print("✅ Data saved as 'zillow_real_estate_data.csv'")
    else:
        print("❌ No property data found in response.")
else:
    print(f"❌ Failed to fetch data. Status Code: {response.status_code}, Message: {response.text}")

print(df.head(10))  # Show the first 10 rows