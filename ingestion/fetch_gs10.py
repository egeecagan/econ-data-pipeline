import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import json
from utils.fred_api import get_series

def fetch_gs10():
    data = get_series("GS10", file_type="json")
    output_path = "data/raw/gs10_raw.json"
    with open(output_path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"GS10 data saved to {output_path}")

if __name__ == "__main__":
    fetch_gs10()
