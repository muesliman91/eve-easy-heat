import json
import requests

NAHOL_ID = 30005069

# Jumps abrufen
jumps = requests.get(
    "https://esi.evetech.net/latest/universe/system_jumps/"
).json()

nahol_jumps = next(
    s for s in jumps
    if s["system_id"] == NAHOL_ID
)

# Kills abrufen
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

result = {
    "system_id": 30005069,
    "name": "Nahol",
    "security": 0.6,
    "region": "Kor-Azor",

    "activity": {
        "jumps": nahol_jumps["ship_jumps"],
        "npc_kills": nahol_kills["npc_kills"],
        "ship_kills": nahol_kills["ship_kills"],
        "pod_kills": nahol_kills["pod_kills"]
    }
}

with open("docs/systems/Nahol.json", "w") as f:
    json.dump(result, f, indent=2)

print(result)
