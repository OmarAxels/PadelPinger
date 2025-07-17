import requests
import datetime

URL = "https://padel-scraper.onrender.com/"

try:
    print(f"[{datetime.datetime.now()}] Pinging {URL}")
    response = requests.get(URL)
    print(f"[{datetime.datetime.now()}] Pinged {URL} - Status: {response.status_code}")
except Exception as e:
    print(f"[{datetime.datetime.now()}] Error: {e}")
