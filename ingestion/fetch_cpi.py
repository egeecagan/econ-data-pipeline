import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import json
from utils.fred_api import get_series

def fetch_cpi():
    # 1) FRED’den ham veriyi çek
    data = get_series("CPIAUCSL", file_type="json")

    # 2) RAW klasörüne kaydet
    output_path = "data/raw/cpi_raw.json"
    with open(output_path, "w") as f:
        json.dump(data, f, indent=4)

    print(f"cpi data saved to {output_path}")

if __name__ == "__main__":
    fetch_cpi()
