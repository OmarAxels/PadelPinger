import requests
import datetime

URL = "https://padel-scraper.onrender.com/"
URL2 = "https://padelvaktin.is/"

try:
    print(f"[{datetime.datetime.now()}] Pinging {URL}")
    response = requests.get(URL)
    print(f"[{datetime.datetime.now()}] Pinged {URL} - Status: {response.status_code}")
except Exception as e:
    print(f"[{datetime.datetime.now()}] Error: {e}")

try:
    print(f"[{datetime.datetime.now()}] Pinging {URL2}")
    response = requests.get(URL2)
    print(f"[{datetime.datetime.now()}] Pinged {URL2} - Status: {response.status_code}")
except Exception as e:
    print(f"[{datetime.datetime.now()}] Error: {e}")

