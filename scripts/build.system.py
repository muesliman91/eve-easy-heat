import json
import glob
from datetime import datetime, timezone, timedelta
from pathlib import Path

NAHOL_ID = 30005069

Path("docs/systems").mkdir(parents=True, exist_ok=True)

now = datetime.now(timezone.utc)

snapshots = []

for filename in glob.glob("snapshots/nahol/*.json"):
    with open(filename) as f:
        snapshot = json.load(f)

    timestamp = datetime.fromisoformat(snapshot["timestamp"])

    snapshots.append({
        "timestamp": timestamp,
        "jumps": snapshot["jumps"],
        "npc_kills": snapshot["npc_kills"],
        "ship_kills": snapshot["ship_kills"],
        "pod_kills": snapshot["pod_kills"]
    })

# Nach Zeit sortieren
snapshots.sort(key=lambda x: x["timestamp"])

# Falls noch keine Snapshots existieren
if not snapshots:
    current = {
        "jumps": 0,
        "npc_kills": 0,
        "ship_kills": 0,
        "pod_kills": 0
    }
else:
    latest = snapshots[-1]

    current = {
        "jumps": latest["jumps"],
        "npc_kills": latest["npc_kills"],
        "ship_kills": latest["ship_kills"],
        "pod_kills": latest["pod_kills"]
    }

# Zeitfenster
last_24h_start = now - timedelta(hours=24)
last_7d_start = now - timedelta(days=7)

snapshots_24h = [
    s for s in snapshots
    if s["timestamp"] >= last_24h_start
]

snapshots_7d = [
    s for s in snapshots
    if s["timestamp"] >= last_7d_start
]

def sum_activity(items):
    return {
        "jumps": sum(s["jumps"] for s in items),
        "npc_kills": sum(s["npc_kills"] for s in items),
        "ship_kills": sum(s["ship_kills"] for s in items),
        "pod_kills": sum(s["pod_kills"] for s in items)
    }

result = {
    "system_id": NAHOL_ID,
    "name": "Nahol",
    "security": 0.6,
    "region": "Kor-Azor",

    "current": current,

    "totals_24h": sum_activity(snapshots_24h),

    "totals_7d": sum_activity(snapshots_7d),

    "snapshot_count": len(snapshots)
}

with open("docs/systems/Nahol.json", "w") as f:
    json.dump(result, f, indent=2)

print(result)
