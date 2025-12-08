import json
import pandas as pd

def clean_cpi():
    raw_path = "data/raw/sp500_raw.json"
    clean_path = "data/clean/sp500_clean.csv"

    with open(raw_path, "r") as f:
        raw = json.load(f)

    df = pd.DataFrame(raw["observations"])
    df = df[["date", "value"]]

    # real time start and end valeus are not important for our goal so i didnt take them
    df["date"] = pd.to_datetime(df["date"])
    df["value"] = pd.to_numeric(df["value"], errors="coerce")

    # delete the rows who contains at least one NaN
    df = df.dropna()

    # save clean data to a csv file
    df.to_csv(clean_path, index=False)

    print(f"sp500 cleaned data saved to {clean_path}")

if __name__ == "__main__":
    clean_cpi()
