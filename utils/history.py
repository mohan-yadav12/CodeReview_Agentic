import json

FILE = ("output/history.json")
def save_history(repo,rows):
    try:
        with open(FILE) as f:
            data = (json.load(f))

    except:
        data = []
    data.append({"repo": repo, "rows": len(rows)})
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)