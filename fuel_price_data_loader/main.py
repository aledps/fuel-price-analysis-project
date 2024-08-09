from utils.load_fuel_watch_api import fetch_and_load_rss_data
from utils.load_discount_excel import load_excel_data
import config

if __name__ == "__main__":
    fetch_and_load_rss_data()
    load_excel_data()

