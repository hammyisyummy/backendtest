import os
import requests

# Store credentials securely
CLIENT_ID = "zalzndjimwb5e6k9vo6pbe37vtbe6n"  # Replace with your actual Client ID
CLIENT_SECRET = "7o2jgjh9m6h0nb5ucyiz93juox1jpr"  # Replace with your actual Client Secret


# Get OAuth Token (Using POST request with form data)
auth_url = "https://id.twitch.tv/oauth2/token"

data = {
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "grant_type": "client_credentials"
}

response1 = requests.post(auth_url, data=data)

if response1.status_code == 200:
    access_token = response1.json().get("access_token")
    print("Access Token:", access_token)
else:
    print("Error getting token:", response1.status_code, response1.text)
    exit()  # Stop execution if token retrieval fails

# IGDB API Request
igdb_url = "https://api.igdb.com/v4/games"  # Corrected endpoint
headers = {
    "Client-ID": CLIENT_ID,
    "Authorization": f"Bearer {access_token}",
}

body = "fields name,genres; limit 5;"  # IGDB API query syntax

response = requests.post(igdb_url, headers=headers, data=body)

if response.status_code == 200:
    print(response.json())  # Output the JSON response
else:
    print("Error:", response.status_code, response.text)