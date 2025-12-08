# 💸 Economic Data Pipeline

## Overview

This project provides a simple data pipeline for downloading, cleaning, and organizing economic time series data from the FRED (Federal Reserve Economic Data) API. The goal is to build a small but realistic data engineering workflow that demonstrates ingestion, cleaning, and integration of macroeconomic datasets.

## Features

* Retrieve time series data from the FRED API using a modular utility function. (`utils/fred_api.py`)
* Store raw data in a structured directory layout.
* Clean and normalize economic datasets for downstream analysis.
* Optional merging of multiple economic indicators into a unified dataset.
* Easily extendable to additional series such as unemployment rate, GDP growth, or interest rates.


## Requirements

* Python 3.10+
* requests
* pandas
* python-dotenv
* jupyter

After creating virtual environment and activating it install dependencies with:

```
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root with the following variable:

```
FRED_API_KEY=your_api_key_here
```

You can obtain an API key from the St. Louis Federal Reserve website. (https://fred.stlouisfed.org/)

## Usage

1. Run the ingestion script to download a series (e.g., CPI):

```
python ingestion/fetch_cpi.py
```

2. Run the cleaning script to convert and normalize the raw dataset:

```
python cleaning/clean_cpi.py
```

3. Run the integration script if combining multiple datasets:

```
python integration/merge_macro.py
```

**This project uses the FRED® API but is not endorsed or certified by the Federal Reserve Bank of St. Louis.**
