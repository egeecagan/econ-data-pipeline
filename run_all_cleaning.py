import subprocess

SCRIPTS = [
    "cleaning/clean_cpi.py",
    "cleaning/clean_unrate.py",
    "cleaning/clean_fedfunds.py",
    "cleaning/clean_gs10.py",
    "cleaning/clean_gdp.py",
    "cleaning/clean_sp500.py",
    "cleaning/clean_m2.py",
    "cleaning/clean_houst.py",
]

def run_all_cleaning():
    print("\nrunning cleaning pipeline\n")

    for script in SCRIPTS:
        print(f"running: {script}")

        result = subprocess.run(["python3", script])

        if result.returncode != 0:
            print(f"error running -> {script}")
            return

        print(f"finished: {script}\n")

    print("\nall cleaning tasks completed successfully")

if __name__ == "__main__":
    run_all_cleaning()
