# Afficionado Coffee Roasters — Sales Trend & Time-Based Performance Dashboard

A Streamlit dashboard using the **Stitch UI as the visual source of truth** and the **Afficionado Coffee Roasters Excel workbook as the data source of truth**.

## Included
- Stitch dashboard UI reproduced inside Streamlit
- Real Excel-backed hourly aggregation
- Store filter for all three stores
- Revenue / transaction metric toggle
- Morning / Noon–Eve / Closing daypart filters
- Operating-hour slider
- Dynamic KPIs
- Hourly demand & revenue analysis
- Peak / lowest demand insights
- Store performance comparison
- Store × hour heatmap with Transactions / Revenue / Quantity
- Category and operational insight sections from the Stitch design
- CSV export of the currently filtered hourly data

## Important data limitation
The workbook contains `year` and `transaction_time`, but no calendar date column. Therefore Monday–Sunday / weekday-vs-weekend analysis is **not invented**. The Day of Week control is visibly disabled until a real calendar date field is available.

## Run on Windows
From the project folder:

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py -m streamlit run app.py
```

If PowerShell blocks activation, you can still install/run without activating:

```powershell
py -m pip install -r requirements.txt
py -m streamlit run app.py
```

The dashboard opens at `http://localhost:8501`.

## Project structure

```text
Afficionado-Coffee-Sales-Dashboard/
├── app.py
├── requirements.txt
├── data/
│   └── Afficionado Coffee Roasters.xlsx
└── assets/
    ├── code.html
    └── DESIGN.md
```
