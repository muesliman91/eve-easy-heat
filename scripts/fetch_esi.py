import requests
import json

NAHOL_ID = 30005069

# Fetch all jumps
jumps = requests.get(
    "https://esi.evetech.net/latest/universe/system_jumps/"
).json()

# Find Nahol
nahol = next(
    x for x in jumps
    if x["system_id"] == NAHOL_ID
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
