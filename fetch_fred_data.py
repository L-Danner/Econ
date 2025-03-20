import requests
import pandas as pd

# FRED API Key (You need to get this from https://fred.stlouisfed.org/)
api_key = "97d3a0a768ad9549b93a55425760ce55"

# Define the FRED series IDs
series_ids = {
    "Corporate Profits": "CP",
    "Labor Force Participation": "CIVPART"
}

# Loop through each series and fetch the data
for name, series_id in series_ids.items():
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={api_key}&file_type=json"
    
    response = requests.get(url)
    data = response.json()
    
    # Extract the observations
    observations = data.get("observations", [])
    
    # Convert to DataFrame
    df = pd.DataFrame(observations)
    
    # Convert date column and values
    df["date"] = pd.to_datetime(df["date"])
    df["value"] = pd.to_numeric(df["value"], errors='coerce')
    
    # Save as CSV file
    filename = f"{series_id}.csv"
    df.to_csv(filename, index=False)
    print(f"Saved {filename}")

print("Data download complete!")
