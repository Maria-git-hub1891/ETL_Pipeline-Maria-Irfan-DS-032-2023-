# ETL_Pipeline_MariaIrfan_DS-032

This project implements a complete **ETL (Extract, Transform, Load)** pipeline using Python. It extracts data from multiple sources (CSV, JSON/API, Google Sheets), processes and cleans the data, and stores the final output in a database-ready format. The notebook `ETL_ASSIGNMENT.ipynb` contains the core logic behind the ETL operations.

---

## 📁 Project Structure

📁 weather-etl-pipeline/
├── weather_etl.py          # Main ETL logic
├── scheduler.py            # Scheduler to run ETL job periodically
├── db_config.json          # MongoDB URI and API key configuration
├── requirements.txt        # Python dependencies
└── README.md               # Project overview


## 🚀 ETL Notebook Overview

The notebook `ETL_ASSIGNMENT (2).ipynb` contains:
- ✅ Reading data from different sources:
  - CSV (`sample_data.csv`)
  - JSON (simulated weather API)
  - Google Sheets (exported as CSV)
- ✅ Cleaning and transforming the data
- ✅ Merging and exporting a final dataset
- ✅ Optional loading into a database (via `load_to_db.py`)


## 🛠️ Setup & Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/ETL_Pipeline_MariaIrfan_DS-032.git
cd ETL_Pipeline_MariaIrfan_DS-032

2. Install dependencies:

pip install -r requirements.txt

python -m venv venv
source venv/bin/activate

3. Automation
Use scheduler.py to automate the ETL pipeline daily using:

schedule Python module (in-script scheduler)


4. CI/CD Integration
The .github/workflows/ci_cd.yml enables GitHub Actions for:

Code linting

Notebook execution tests

Future deployment hooks

5. Run the ETL Pipeline
python weather_etl.py

6. Run the Scheduler
python scheduler.py

🔄 Automation
Use scheduler.py to automate the ETL pipeline daily using:

schedule Python module (in-script scheduler)

Or set up as a cron job for system-level automation

🧪 CI/CD Integration
The .github/workflows/ci_cd.yml enables GitHub Actions for:

Code linting

Notebook execution tests

Future deployment hooks

🧰 Technologies Used
Python (pandas, json, requests, etc.)

Jupyter Notebook

Git & GitHub

GitHub Actions (CI/CD)

CSV, JSON, Google Sheets

📄 License
This project is for academic use only. Please contact the author for other use cases.

👤 Author
Maria Irfan
Roll Number: DS-032-2023
