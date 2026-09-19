import requests
import sys

with open("sites.txt") as f:
    sites = [line.strip() for line in f if line.strip()]

for site in sites:
    try:
        response = requests.get(site, timeout=5)
        print(f"{site} is UP (status {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"{site} is DOWN - {e}")
