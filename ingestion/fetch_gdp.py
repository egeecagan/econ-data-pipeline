import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from utils.fred_api import get_series

def fetch_gdp():
    data = get_series("GDPC1", file_type="json")
    output_path = "data/raw/gdp_raw.json"
    with open(output_path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"GDP data saved to {output_path}")

if __name__ == "__main__":
    fetch_gdp()
