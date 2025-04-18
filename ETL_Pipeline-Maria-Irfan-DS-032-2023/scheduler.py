import schedule
import time
import os
import subprocess

def run_notebook():
    print("Running ETL notebook...")
    result = subprocess.run([
        "jupyter", "nbconvert", "--to", "notebook", 
        "--execute", "--inplace", "ETL_ASSIGNMENT.ipynb"
    ])
    if result.returncode == 0:
        print("Notebook ran successfully!")
    else:
        print("Error running notebook.")

# Schedule the notebook to run every day at 8 AM
schedule.every().day.at("08:00").do(run_notebook)

print("Scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(60)
