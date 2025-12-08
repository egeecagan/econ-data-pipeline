import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import json
from utils.fred_api import get_series

def fetch_unrate():
    data = get_series("UNRATE", file_type="json")
    output_path = "data/raw/unrate_raw.json"
    with open(output_path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"UNRATE data saved to {output_path}")


if __name__ == "__main__":
    fetch_unrate()
