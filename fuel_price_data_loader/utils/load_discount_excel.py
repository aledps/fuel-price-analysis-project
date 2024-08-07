import os
import pandas as pd
from utils.connection import get_snowflake_connection
import config

def load_excel_data():
    # Construct the full file path
    excel_file_path = os.path.join(config.EXCEL_FILE_PATH, config.EXCEL_FILE_NAME)

    # Check if the file exists
    if not os.path.exists(excel_file_path):
        print(f"Excel file not found at path: {excel_file_path}")
        return

    # Read data from the Excel file
    try:
        df = pd.read_excel(excel_file_path)
    except Exception as e:
        print(f"Error reading the Excel file: {e}")
        return

    # Check if the DataFrame is empty
    if df.empty:
        print(f"The Excel file is empty: {excel_file_path}")
        return

    # Initialize an empty list to store transformed data
    transformed_data = []

    # Iterate over the columns to get the data
    for column in df.columns:
        brand_name = column
        discount = float(df[column].iloc[0]) if not pd.isna(df[column].iloc[0]) else None

        # Append the brand and discount value to the list
        transformed_data.append((brand_name, discount))

    conn = get_snowflake_connection()
    if conn is None:
        return

    #Insert the transformed data into the Snowflake table
    excel_insert_query = f"""
    INSERT INTO {config.SNOWFLAKE_DATABASE}.{config.SNOWFLAKE_SCHEMA}.{config.SNOWFLAKE_DISCOUNT_TABLE} (
        BRAND, DISCOUNT) VALUES (%s, %s)"""


    cursor = conn.cursor()
    cursor.executemany(excel_insert_query, transformed_data)
    conn.commit()

    cursor.close()
    conn.close()

    print("Excel data inserted successfully.")
