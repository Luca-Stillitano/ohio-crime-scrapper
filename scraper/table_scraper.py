# Author: Taaj Stillitano
# Email: Stillitano.engineering@gmail.com
# Date Created: 1/26/2026
# Date Last Updated: 1/26/2026

"""
Purpose:
This file contains functions to scrape data from the Ohio crime data table generated
on the website. It returns the data as a structured list of dictionaries or optionally
as a Pandas DataFrame for further analysis or saving.
"""

from playwright.async_api import Page
from typing import List, Dict
import pandas as pd


async def scrape_table(page: Page) -> List[Dict[str, str]]:
    """
    Scrape the main table from the current page.

    INPUTS:
    - page: Playwright Page object with the table already generated

    OUTPUTS:
    - data: List of dictionaries, each representing a row with column headers as keys
    """
    table = page.locator("table.table-striped")

    # Get headers
    headers = await table.locator("thead th").all_inner_texts()
    headers = [h.strip() for h in headers]

    # Get all rows
    rows = table.locator("tbody tr")
    row_count = await rows.count()

    data = []
    for i in range(row_count):
        row = rows.nth(i)
        cells = await row.locator("td").all_inner_texts()
        cells = [c.strip() for c in cells]

        # Skip malformed rows
        if len(cells) != len(headers):
            continue

        record = dict(zip(headers, cells))
        data.append(record)

    return data

def table_to_dataframe(data: List[Dict[str, str]]) -> pd.DataFrame:
    """
    Convert the scraped table list of dictionaries into a Pandas DataFrame.

    INPUTS:
    - data: List of dictionaries representing table rows

    OUTPUTS:
    - df: Pandas DataFrame with table headers as columns
    """
    df = pd.DataFrame(data)
    return df
