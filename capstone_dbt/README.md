# End-to-End E-Commerce Analytics Pipeline

An end-to-end data pipeline that takes raw, messy e-commerce data and turns it into clean, tested, analysis-ready tables in a cloud warehouse, then pulls insights back out. Built with Python, BigQuery, and dbt.

## What it does

Raw messy CSVs get cleaned with Python, loaded to BigQuery, transformed with dbt into tested analytics marts, then analyzed with Python for business insights.

```
raw CSVs  ->  Python (clean)  ->  BigQuery (load)  ->  dbt (transform)  ->  Python (analyze)
 messy        standardize,         cloud warehouse      staging + marts      insights &
 data         dedupe, fix          (raw tables)         + tests + docs       findings
              types, nulls
```

## The stack

- **Python / pandas** for data cleaning (ingestion) and analysis (insights)
- **BigQuery** as the cloud data warehouse
- **dbt** for the transformation layer (staging to marts), with tests, documentation, and lineage
- **SQL** for the transformations (joins, aggregations, date logic)
- **Git** for version control

## Pipeline steps

### 1. Clean (`clean_data.py`)
Takes deliberately messy raw data (`raw_customers.csv`, `raw_orders.csv`) with inconsistent casing and whitespace, mixed date formats, missing values, duplicate rows, and dollar amounts stored as text. Cleans it with pandas by deduplicating, standardizing text, handling missing values, and fixing data types. Outputs `cleaned_customers.csv` and `cleaned_orders.csv`.

### 2. Load (`load_to_bigquery.py`)
Loads the cleaned data into BigQuery (dataset: `capstone_raw`) as raw tables, using `pandas-gbq`.

### 3. Transform (`capstone_dbt/`)
A dbt project that transforms the raw BigQuery tables into analytics-ready marts:
- **Sources**: the raw BigQuery tables, declared for lineage
- **Staging models** (`stg_customers`, `stg_orders`): clean, standardized views over the raw sources
- **Marts** (built as tables):
  - `customer_metrics`: per-customer total spend, order count, and average order value, joined with customer name and city
  - `revenue_over_time`: monthly revenue, order count, and average order value
- **Tests**: `unique` and `not_null` checks on keys
- **Docs and lineage**: generated with `dbt docs`, showing the full source to staging to marts graph

### 4. Analyze (`analysis.py`)
Pulls the finished marts back into pandas and surfaces business insights (top customers, revenue trends, per-city spending, and what drives revenue). Findings are written up in `findings.md`.

## Key findings

See [`findings.md`](findings.md) for the full write-up. Highlights:
- One market leads on total spend, but another has the highest-value individual customers, showing different segments that need different strategies.
- Order volume is stable month to month, but revenue swings with average order value, meaning revenue growth is driven by order value rather than order count.
- A small group of high-value customers drives an outsized share of revenue.

## Running it

Requires Python, a dbt project connected to BigQuery, and `pandas`, `pandas-gbq`, `dbt-bigquery`.

```bash
python clean_data.py          # 1. clean raw data
python load_to_bigquery.py    # 2. load to BigQuery
cd capstone_dbt
dbt run                       # 3. build staging + marts
dbt test                      # run data-quality tests
dbt docs generate             # generate docs + lineage
cd ..
python analysis.py            # 4. pull marts back + analyze
```

## Notes

Built as a hands-on project to practice the modern data stack end to end. The dataset is generated sample data, deliberately given realistic messiness so the cleaning and staging layers do genuine work. The architecture (raw to staging to marts, with tests and documentation, on a cloud warehouse) mirrors how production data pipelines are structured.