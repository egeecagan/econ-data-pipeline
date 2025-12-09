import pandas as pd
import sqlite3, os
from pathlib import Path
from pandas.tseries.offsets import MonthBegin
# from sqlalchemy import create_engine

# macros
DATA_CLEAN = Path("data/clean")
OUTPUT_CSV = Path("data/final/macro_dataset.csv")
OUTPUT_SQLITE = Path("data/final/macro_data.db")
SQL_TABLE_NAME = "macro_dataset"

# if you want to write to some db except sqlite use this parameter like below
# also do not forget to delete # before from sqlalchemy ... 
SQL_ENGINE = None # create_engine("protocol username password etc... like a url idk")

def load_series(filename):
    df = pd.read_csv(os.path.join(DATA_CLEAN, filename))

    # type casting string to datetime obj from pandas
    df["date"] = pd.to_datetime(df["date"])
    df = df.set_index("date").sort_index()

    s = df["value"]
    return s


print("loading clean series ..")

cpi = load_series("cpi_clean.csv")
fedfunds = load_series("fedfunds_clean.csv")
gs10 = load_series("gs10_clean.csv")
houst = load_series("houst_clean.csv")
unrate = load_series("unrate_clean.csv")
m2 = load_series("m2_clean.csv")
sp500 = load_series("sp500_clean.csv")
gdp = load_series("gdp_clean.csv")

print("all series loaded")

print("resampling series to monthly ..")

# for ex u have 15 th day of january it moves it to 1st of january you do not lose any info just move
def to_monthly(s):
    return s.resample("MS").ffill()  # ms stands for monthly start
    # lets say you have january and march no feb ffil makes feb value equal to jan value (forward fill)

# monthly -> monthly
cpi_m = to_monthly(cpi)
fedfunds_m = to_monthly(fedfunds)
gs10_m = to_monthly(gs10)
houst_m = to_monthly(houst)
unrate_m = to_monthly(unrate)
m2_m = to_monthly(m2)

# quarterly -> monthly
gdp_m = gdp.resample("MS").ffill()

sp500_m = sp500.resample("ME").last()

sp500_m.index = (sp500_m.index + MonthBegin(-1)).normalize()

print("merging all series ..")

df = pd.DataFrame({
    "cpi": cpi_m,
    "fedfunds": fedfunds_m,
    "gs10": gs10_m,
    "houst": houst_m,
    "unrate": unrate_m,
    "m2": m2_m,
    "gdp": gdp_m,
    "sp500": sp500_m
})

df = df.sort_index()

OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_CSV)
print(f"csv written to {OUTPUT_CSV}")


conn = sqlite3.connect(OUTPUT_SQLITE)
df.to_sql(SQL_TABLE_NAME, conn, if_exists="replace", index=True)
conn.close()
print(f"sqlite db written to {OUTPUT_SQLITE}")


if SQL_ENGINE is not None:
    df.to_sql(SQL_TABLE_NAME, SQL_ENGINE, if_exists="replace", index=True)
    print("data written to sql database via sqlalchemy.")


print("integration is done")
