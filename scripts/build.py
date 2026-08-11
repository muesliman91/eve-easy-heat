import json
import glob

history = []

for file in sorted(glob.glob("data/*.json")):

    with open(file) as f:
        snapshot = json.load(f)

    total_jumps = sum(x["ship_jumps"] for x in snapshot)

    history.append({
        "date": file.split("/")[-1].replace(".json", ""),
        "jumps": total_jumps
    })

with open("docs/activity.json", "w") as f:
    json.dump(history, f)
