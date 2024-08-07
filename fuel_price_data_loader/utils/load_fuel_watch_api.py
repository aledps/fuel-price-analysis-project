import requests
from utils.rss_parser import parse_rss_feed
from utils.connection import get_snowflake_connection
import config

def fetch_and_load_rss_data():
    # Step 1: Fetch the RSS data from the API
    url = 'https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        rss_data = response.content
        print("RSS data fetched successfully.")
    else:
        print(f"Failed to retrieve RSS data. Status code: {response.status_code}")
        return # Exit the function if the response status code is not 200

    # Step 2: Parse the RSS feed to extract relevant data
    if rss_data:
        rss_data_list = parse_rss_feed(rss_data)
    else:
        rss_data_list = []

    # Step 3: Insert the data into the Snowflake table, if rss_data_list has data
    if rss_data_list:
        conn = get_snowflake_connection()
        if conn is None:
            return

        insert_query = f"""
        INSERT INTO {config.SNOWFLAKE_DATABASE}.{config.SNOWFLAKE_SCHEMA}.{config.SNOWFLAKE_GAS_STATION_TABLE} (
            TITLE, DESCRIPTION, BRAND, DATE, PRICE, TRADING_NAME, LOCATION, ADDRESS, PHONE, LATITUDE, LONGITUDE, SITE_FEATURES
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor = conn.cursor()
        cursor.executemany(insert_query, rss_data_list)
        conn.commit()

        cursor.close()
        conn.close()

        print("RSS data inserted successfully.")
