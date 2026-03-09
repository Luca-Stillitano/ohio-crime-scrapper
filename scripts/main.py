#Author: Taaj Stillitano
#Email: Stillitano.engineering@gmail.com
#Date Created: 1/26/2026
#Date Last Updated: 1/26/2026

"""
Purpose:
Main entry point for the Ohio crime data scraper. This script orchestrates the following:

- Launching the browser
- Selecting dropdown options (report type, year, time period)
- Clicking the 'Get Report' button
- Scraping the generated table using table_scraper.py
- Downloading the generated Excel report using download_actions.py (for testing)

Contents:
- run_scraper: main async function to perform scraping
- main: synchronous entry point for testing, now also tests download
"""

from config.settings import data_folder
from scraper.browser_actions import launch_browser, select_dropdown_options, click_get_report
#from scraper.table_scraper import scrape_table #validation purposes
from scraper.download_actions import download_report
from playwright.async_api import async_playwright
import asyncio

# Define where to save the downloaded Excel file for testing
download_file_path = data_folder+"/ohio_crime_report.ods"

async def run_scraper():
    async with async_playwright() as p:  # keep Playwright context alive
        page, browser = await launch_browser(p)
        await select_dropdown_options(page)
        await click_get_report(page)

        # Test scraping table (kept for full functionality)
        #data = await scrape_table(page)

        # Test download functionality
        df = await download_report(page, str(download_file_path))
        print(f"Downloaded Excel file saved to: {download_file_path}")
        print('Sample Table: ')
        print(df.head())

        await browser.close()
        #return data
        return None

if __name__ == "__main__":
    scraped_data = asyncio.run(run_scraper())
    #print("Sample scraped rows:")
    #print(scraped_data[:3])
