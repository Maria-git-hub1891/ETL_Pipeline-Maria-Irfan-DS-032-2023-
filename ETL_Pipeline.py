mkdir -p ETL_Pipeline_MariaIrfan_Ds-032/{config,data,output,.github/workflows}
cd ETL_Pipeline_MariaIrfan_Ds-032

# Create files
touch etl_pipeline.py scheduler.py requirements.txt README.md load_to_db.py report.pdf
touch config/db_config.json
touch data/sample_data.csv data/sample_weather.json data/google_sheet_sample.csv
touch output/final_cleaned_data.csv
touch .github/workflows/ci_cd.yml
