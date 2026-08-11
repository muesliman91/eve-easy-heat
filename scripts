import requests
import json
from datetime import datetime

url = "https://esi.evetech.net/latest/universe/system_jumps/"

data = requests.get(url).json()

today = datetime.utcnow().strftime("%Y-%m-%d")

with open(f"data/{today}.json", "w") as f:
    json.dump(data, f)
