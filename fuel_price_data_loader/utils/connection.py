# connection.py

import snowflake.connector
import config

def get_snowflake_connection():
    try:
        conn = snowflake.connector.connect(
            user=config.SNOWFLAKE_USER,
            password=config.SNOWFLAKE_PASSWORD,
            account=config.SNOWFLAKE_ACCOUNT
        )
        return conn
    except Exception as e:
        print(f"Error connecting to Snowflake: {e}")
        return None
