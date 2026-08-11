import json
import requests
from datetime import datetime
from pathlib import Path

snapshot = {
    "timestamp": datetime.utcnow().isoformat(),
    "jumps": requests.get(
        "https://esi.evetech.net/latest/universe/system_jumps/"
    ).json(),

    "kills": requests.get(
        "https://esi.evetech.net/latest/universe/system_kills/"
    ).json()
}

Path("snapshots").mkdir(exist_ok=True)

filename = (
    datetime.utcnow().strftime("%Y-%m-%d")
    + ".json"
)

with open(f"snapshots/{filename}", "w") as f:
    json.dump(snapshot, f)
