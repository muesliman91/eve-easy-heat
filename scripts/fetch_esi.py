import json
import requests
from datetime import datetime, timezone
from pathlib import Path

NAHOL_ID = 30005069

# Ordner für Snapshots erstellen
Path("snapshots/nahol").mkdir(parents=True, exist_ok=True)

# Aktuelle UTC-Zeit
now = datetime.now(timezone.utc)

# Jumps von ESI abrufen
jumps = requests.get(
    "https://esi.evetech.net/latest/universe/system_jumps/"
).json()

nahol_jumps = next(
    s for s in jumps
    if s["system_id"] == NAHOL_ID
)

# Kills von ESI abrufen
kills = requests.get(
    "https://esi.evetech.net/latest/universe/system_kills/"
).json()

nahol_kills = next(
    (
        s for s in kills
        if s["system_id"] == NAHOL_ID
    ),
    {
        "npc_kills": 0,
        "ship_kills": 0,
        "pod_kills": 0
    }
)

# Ein Stunden-Snapshot
snapshot = {
    "timestamp": now.isoformat(),
    "system_id": NAHOL_ID,
    "jumps": nahol_jumps["ship_jumps"],
    "npc_kills": nahol_kills["npc_kills"],
    "ship_kills": nahol_kills["ship_kills"],
    "pod_kills": nahol_kills["pod_kills"]
}

# Dateiname pro Stunde
filename = now.strftime("%Y-%m-%d-%H") + ".json"

with open(f"snapshots/nahol/{filename}", "w") as f:
    json.dump(snapshot, f, indent=2)

print(snapshot)
