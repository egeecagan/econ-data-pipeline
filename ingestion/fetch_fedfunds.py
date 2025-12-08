import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from utils.fred_api import get_series

def fetch_fedfunds():
    data = get_series("FEDFUNDS", file_type="json")
    output_path = "data/raw/fedfunds_raw.json"
    with open(output_path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"FEDFUNDS data saved to {output_path}")

if __name__ == "__main__":
    fetch_fedfunds()