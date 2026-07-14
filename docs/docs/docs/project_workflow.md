# Project Workflow

This project follows a complete end-to-end data analytics workflow, starting from raw sales data and ending with an interactive Power BI dashboard.

---

## Step 1: Data Collection

- Imported the Global Superstore sales dataset in CSV format.
- Verified the dataset structure and available columns.

**Input:** `data/raw/superstore.csv`

---

## Step 2: Data Validation

Python was used to perform initial data validation.

Validation checks included:

- Dataset shape
- Column names
- Missing values
- Duplicate records
- Preview of the dataset

**Script:** `python/01_data_validation.py`

---

## Step 3: Data Cleaning

The raw dataset was cleaned and prepared for analysis.

Cleaning tasks included:

- Removing unnecessary columns
- Renaming column names
- Converting date columns
- Saving the cleaned dataset

**Script:** `python/02_data_cleaning.py`

---

## Step 4: Data Quality Report

A quality report was generated to verify the cleaned dataset.

Checks included:

- Missing values
- Duplicate records
- Data types
- Memory usage

**Script:** `python/03_data_quality_report.py`

---

## Step 5: SQL Server Database

A normalized relational database was created in SQL Server.

Database Tables:

- Customers
- Products
- Orders
- Locations
- Sales

Primary keys and foreign keys were used to maintain data integrity.

---

## Step 6: Load Data into SQL Server

The cleaned dataset was loaded into SQL Server using Python and PyODBC.

**Script:** `python/04_load_to_sql.py`

---

## Step 7: Business Analysis using SQL

SQL queries were written to analyze business performance.

Analysis included:

- Total Sales
- Total Profit
- Sales by Category
- Sales by Market
- Sales by Region
- Top Customers
- Top Products
- Profit Margin
- Average Order Value
- Product Ranking

**Script:** `database/03_analysis_queries.sql`

---

## Step 8: Power BI Dashboard

The SQL database was connected to Power BI to build interactive dashboards.

Dashboard Pages:

- Executive Overview
- Sales Analysis
- Customer Analysis
- Product Analysis
- Executive Insights

---

## Step 9: Business Insights

The final dashboard helps stakeholders understand:

- Sales performance
- Customer behavior
- Product performance
- Regional trends
- Business KPIs

---

## Project Flow

```text
Raw CSV Dataset
        │
        ▼
Python Validation
        │
        ▼
Python Data Cleaning
        │
        ▼
SQL Server Database
        │
        ▼
Business SQL Queries
        │
        ▼
Power BI Dashboard
        │
        ▼
Business Insights
```