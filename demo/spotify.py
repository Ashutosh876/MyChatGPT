import requests
import os

# Ask the user for the endpoint and HTTP method
endpoint = input("Enter the endpoint: ")
http_method = input("Enter the HTTP method (GET or POST): ").upper()

#base url
base_url = "https://api.spotify.com/v1/"

# Set the access token
SPOTIFY_ACCESS_TOKEN = os.getenv("SPOTIFY_ACCESS_TOKEN")

# Set the headers
headers = {
    "Authorization": f"Bearer {SPOTIFY_ACCESS_TOKEN}"
}

# Build the complete URL for the API request
url = base_url + endpoint

# Send the appropriate request to the endpoint
if http_method == "GET":
    response = requests.get(url, headers=headers)
elif http_method == "POST":
    response = requests.post(url, headers=headers)
elif http_method == "PUT":
    track_uri = input("Enter the trackuri: ")
    # Set the JSON body with the track URI
    json_data = {
        "uris": [track_uri]
    }
    response = requests.put(url, headers=headers, json=json_data)
else:
    print("Error: Invalid HTTP method entered.")
    exit()

# Check the response status code to make sure the request was successful
if response.ok:
    print("Request successful.")
else:
    print("Error: Unable to send request.")

# Print the response content
print(response.content)
