import subprocess

SCRIPT = "integration/integrate_and_load.py"

def run_all():
    print("\nrunning integration script\n")

    print(f"running: {SCRIPT}")
    result = subprocess.run(["python3", SCRIPT])

    if result.returncode != 0:
        print(f"error running -> {SCRIPT}")
        return

    print(f"finished: {SCRIPT}\n")

print("\nintegration task completed successfully")

if __name__ == "__main__":
    run_all()
