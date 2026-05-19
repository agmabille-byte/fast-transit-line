from bs4 import BeautifulSoup
import requests

def extract_tracking_data(url):

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers, timeout=10)

    if r.status_code != 200:
        return None

    soup = BeautifulSoup(r.text, "lxml")

    text = soup.get_text(" ", strip=True)

    data = {
        "raw": text,
        "vessel": None,
        "eta": "UNKNOWN",
        "etd": "UNKNOWN",
        "pol": "UNKNOWN",
        "pod": "UNKNOWN"
    }

    return data
