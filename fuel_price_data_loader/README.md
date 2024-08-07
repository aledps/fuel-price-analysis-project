# Fuel Price Data Loader

This project fetches fuel price data from the FuelWatch RSS feed and loads it into a Snowflake table.

## Setup

1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

2. Configure your Snowflake credentials in `config.py`.

3. Run the data loader:
    ```
    python data_loader.py
    ```

## Requirements

- Python 3.7+
- `requests`
- `snowflake-connector-python`