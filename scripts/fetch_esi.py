import json
import requests

NAHOL_ID = 30005069

response = requests.get(
    "https://esi.evetech.net/latest/universe/system_jumps/"
)

systems = response.json()

nahol = next(
    s for s in systems
    if s["system_id"] == NAHOL_ID
)

result = {
    "system_id": 30005069,
    "name": "Nahol",
    "security": 0.6,
    "region": "Kor-Azor",
    "activity": {
        "jumps": nahol["ship_jumps"]
    }
}

with open("docs/systems/Nahol.json", "w") as f:
    json.dump(result, f, indent=2)

print(result)
