import subprocess

SCRIPTS = [
    "ingestion/fetch_cpi.py",
    "ingestion/fetch_unrate.py",
    "ingestion/fetch_fedfunds.py",
    "ingestion/fetch_gs10.py",
    "ingestion/fetch_gdp.py",
    "ingestion/fetch_sp500.py",
    "ingestion/fetch_m2.py",
    "ingestion/fetch_houst.py",
]

def run_all():
    print("\nrunning ingestion pipeline\n")

    for script in SCRIPTS:
        print(f"running: {script}")
        result = subprocess.run(["python3", script])

        if result.returncode != 0:
            print(f"error running -> {script}")
            return

        print(f"Finished: {script}\n")

    print("\nall ingestion tasks completed successfully")

if __name__ == "__main__":
    run_all()
