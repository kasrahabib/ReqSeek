import json
import glob

def clean_notebook(path: str):
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    # remove broken widgets metadata if exists
    nb.get("metadata", {}).pop("widgets", None)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    print(f"✅ Cleaned {path}")

if __name__ == "__main__":
    for f in glob.glob("*.ipynb"):  # only current directory
        clean_notebook(f)

