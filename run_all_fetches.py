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
    print("\n--- Running ingestion pipeline ---\n")

    for script in SCRIPTS:
        print(f"Running: {script}")
        result = subprocess.run(["python3", script])

        if result.returncode != 0:
            print(f"Error running {script}")
            return

        print(f"Finished: {script}\n")

    print("\n--- All ingestion tasks completed successfully! ---")

if __name__ == "__main__":
    run_all()
