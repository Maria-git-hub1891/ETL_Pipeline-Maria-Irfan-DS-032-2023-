# ETL_Pipeline_MariaIrfan_DS-032

This project implements a complete **ETL (Extract, Transform, Load)** pipeline using Python. It extracts data from multiple sources (CSV, JSON/API, Google Sheets), processes and cleans the data, and stores the final output in a database-ready format. The notebook `ETL_ASSIGNMENT (2).ipynb` contains the core logic behind the ETL operations.

---

## 📁 Project Structure

ETL_Pipeline_MariaIrfan_DS-032/ ├── etl_pipeline.py # ETL main script ├── config/ │ └── db_config.json # Dummy database and API keys ├── data/ │ ├── sample_data.csv # Example CSV dataset │ ├── sample_weather.json # Example JSON/API dataset │ └── google_sheet_sample.csv # Exported Google Sheets example ├── scheduler.py # Scheduler for daily ETL automation ├── requirements.txt # Python package dependencies ├── README.md # Project documentation ├── output/ │ └── final_cleaned_data.csv # Processed final output ├── load_to_db.py # Script to load data into a database ├── .github/ │ └── workflows/ │ └── ci_cd.yml # GitHub Actions workflow for CI/CD └── report.pdf


## 🚀 ETL Notebook Overview

The notebook `ETL_ASSIGNMENT (2).ipynb` contains:
- ✅ Reading data from different sources:
  - CSV (`sample_data.csv`)
  - JSON (simulated weather API)
  - Google Sheets (exported as CSV)
- ✅ Cleaning and transforming the data
- ✅ Merging and exporting a final dataset
- ✅ Optional loading into a database (via `load_to_db.py`)

📁 weather-etl-pipeline/
├── weather_etl.py         # Main ETL logic
├── scheduler.py           # Scheduler to run ETL job periodically
├── db_config.json         # MongoDB URI and API key configuration
├── requirements.txt       # Python dependencies
└── README.md              # Project overview

## 🛠️ Setup & Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/ETL_Pipeline_MariaIrfan_DS-032.git
cd ETL_Pipeline_MariaIrfan_DS-032
Install dependencies:


pip install -r requirements.txt

python -m venv venv
source venv/bin/activate

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

📈 Output
Final cleaned and merged dataset is printed to console
Data is stored in MongoDB 
Ready for analytics and visualizations


📄 License
This project is for academic use only. Please contact the author for other use cases.

👤 Author
Maria Irfan
Roll Number: DS-032-2023
