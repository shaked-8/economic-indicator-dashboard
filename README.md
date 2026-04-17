# Economic Indicator Dashboard

A Python-based data analysis tool that retrieves and visualizes macroeconomic indicators using the World Bank API.

## Overview
This project allows users to compare GDP growth across multiple countries over time.  
It demonstrates data collection, cleaning, analysis, and visualization in a structured workflow.

## Features
- Fetches real-world economic data via API
- Supports multiple country comparisons
- Calculates summary statistics (mean, min, max)
- Generates time-series visualizations

## Tech Stack
- Python
- pandas
- matplotlib
- requests

## How to Run

```bash
pip install pandas requests matplotlib
python main.py
```

## Example Usage

Input:
US;IL;DE

Output:
- GDP growth comparison chart
- Summary statistics table

## Data Source
World Bank Open Data API

## Future Improvements
- Add additional indicators (inflation, unemployment)
- Build an interactive dashboard (Streamlit)
- Deploy as a web application
