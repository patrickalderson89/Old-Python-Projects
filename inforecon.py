#!/usr/bin/python3

import sys
import requests
import socket
import json

if len(sys.argv) != 2:
    print(f"\nUsage: \n\t{sys.argv[0][2::]} <url>.")
    sys.exit(1)

url = sys.argv[1]

response = requests.get(f"\n{url}")

# Headers
print("Headers info:\n")
for key in response.headers:
    print(f"{key} : {response.headers[key]}")

# Status
if str(response.status_code) != "400":
    print(f"\nStatus: {response.status_code} - Found")
else:
    print(f"\nStatus: {response.status_code} - Not Found")

# IP
get_host = socket.gethostbyname(url)
print(f"\nIP: {get_host}")

# Location from ipinfo.io
get_location = requests.get(f"https://ipinfo.io/{get_host}/json")
loct_resp = json.loads(get_location.text)

# printo info about location
print(f"\nCountry: {loct_resp['country']} ")
print(f"Region: {loct_resp['region']} ")
print(f"City: {loct_resp['city']} ")
print(f"Postal: {loct_resp['postal']} ")
print(f"Timezone: {loct_resp['timezone']} ")
