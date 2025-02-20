import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of USAID open data
url = "https://data.usaid.gov/browse"

print(f"Fetching data from {url}...")

# Fetch page content
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully fetched data. Parsing HTML...")
else:
    print(f"Failed to fetch data. Status Code: {response.status_code}")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

# Extract dataset links
datasets = []
for link in soup.find_all("a", href=True):
    if "/dataset/" in link["href"]:
        datasets.append("https://data.usaid.gov" + link["href"])

# Debugging: Check if datasets were found
if datasets:
    print(f"Found {len(datasets)} datasets.")
else:
    print("No datasets found.")

# Convert to DataFrame and print
df = pd.DataFrame(datasets, columns=["Dataset Links"])
print(df)

# Save to CSV
df.to_csv("usaid_datasets.csv", index=False)
print("Saved dataset links to usaid_datasets.csv")
