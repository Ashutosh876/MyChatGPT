import requests

# Ask the user for the endpoint and HTTP method
endpoint = input("Enter the endpoint: ")
http_method = input("Enter the HTTP method (GET or POST): ").upper()

#base url
base_url = "https://api.spotify.com/v1/"

# Set the access token
access_token = 'BQDL04XabBYowxQYQXDEj4B5qfrQoD_Q9MMeiy4VpCcx8QgpcYDHVWg7IOxB1vpq3eL8V54RGphc--T3B3wUfc4dp20acFHxsZpSpX76O5vl1jWgt7yuN2rzwfdmCC0VnsvfSJl9S2E58W5V2fcnc37AeonF27skQAxTbGM2IIWcgKlRNDzIyHTmVlY_samdQIGTQAhoX2cnDOnkOtIB2fNbn1dLkMIUswfDfHevdtLBAcvDaHYLOzjCpE7a-A_SMCwwxsc_wDmof46AkzMf7El_58L_494zvIqSMs8QnLf8FEiEsg8mdkBv3nOUZkiEhQcQ-6TqNajnI-tNFeY3c1o9S-dG6j53YQojOYVPNWivs0tDsCQ';

# Set the headers
headers = {
    "Authorization": f"Bearer {access_token}"
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
