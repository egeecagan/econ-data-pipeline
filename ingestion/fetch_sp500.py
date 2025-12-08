import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import json
from utils.fred_api import get_series

def fetch_sp500():
    data = get_series("SP500", file_type="json")
    output_path = "data/raw/sp500_raw.json"
    with open(output_path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"SP500 data saved to {output_path}")


if __name__ == "__main__":
    fetch_sp500()
