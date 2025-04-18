# ETL_Pipeline_MariaIrfan_DS-032

This project implements a complete **ETL (Extract, Transform, Load)** pipeline using Python. It extracts data from multiple sources (CSV, JSON/API, Google Sheets), processes and cleans the data, and stores the final output in a database-ready format. The notebook `ETL_ASSIGNMENT.ipynb` contains the core logic behind the ETL operations.

---

## 📁 Project Structure

📁 weather-etl-pipeline/

├── weather_etl.py      

├── db_config.json         


├──  scheduler.py          

├── requirements.txt       

└── README.md              


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
CSV, JSON, Google Sheets

Code linting

Notebook execution tests

Future deployment hooks

5. Run the ETL Pipeline
python weather_etl.py

6. Run the Scheduler
python scheduler.py


