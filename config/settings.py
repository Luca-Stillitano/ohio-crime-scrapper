# Author: Taaj Stillitano
# Email: Stillitano.engineering@gmail.com
# Date Created: 1/26/2026
# Date Last Updated: 1/26/2026

"""
Purpose:
This file contains global configuration settings for the Ohio crime scraper project. 
It includes URLs, dropdown selections, wait times, file paths, and browser settings.

These variables are intended to be imported into scraper scripts to avoid hardcoding
values, allowing easier maintenance and future modifications.
"""

# Base URL for the Ohio crime data website
base_url: str = "https://dpsoibrspext.azurewebsites.net/?handler=Search"

# Dropdown selections for scraping
report_type: str = "Crimes Reported by County Sheriffs' Offices"
year: str = "2022"
time_period: str = "January-June only"

# Wait times in milliseconds (used between actions to allow page updates)
page_load_wait: int = 2000
table_generation_wait: int = 15000
post_action_wait: int = 2000

# Paths for storing scraped data
data_folder: str = "data/downloads/"
csv_filename: str = "ohio_crime_data.csv"

# Browser configuration
headless: bool = False  # True for headless mode, False to show the browser window

