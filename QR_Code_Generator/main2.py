import requests

ip_address = "127.0.0.1"  # Əldə etdiyin IP ünvanı
response = requests.get(f"https://ipinfo.io/{ip_address}/json")
print(response.json())
