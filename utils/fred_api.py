import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("FRED_API_KEY")

BASE_URL = "https://api.stlouisfed.org/fred/series/observations"
# for fred there are several other api endpoints we could use but this directly returns economic data


def get_series(series_id, file_type="json"):
    file_type = file_type.lower()

    supported_types = ["json", "csv", "xml", "xlsx"]
    if file_type not in supported_types:
        raise ValueError(f"unsupported file_type '{file_type}', supported: {supported_types}")
    
    if file_type in ["xml", "csv", "xlsx"]:
        return "not yet"

    params = {
        "series_id": series_id,
        "api_key": API_KEY,
        "file_type": file_type,
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        raise Exception(
            f"fred api request failed ({response.status_code}): {response.text}"
        )

    if file_type == "json":
        return response.json()             

    elif file_type in ["csv", "xml"]:
        return "not yet"

    elif file_type == "xlsx":
        return "not yet"


print(get_series("CPIAUCSL", "json"))