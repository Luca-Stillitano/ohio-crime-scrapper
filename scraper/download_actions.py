#Author: Taaj Stillitano
#Email: Stillitano.engineering@gmail.com
#Date Created: 1/26/2026
#Date Last Updated: 1/26/2026

"""
Purpose:
This module handles downloading the generated report from the Ohio DPSO website (or similar sources)
directly via Playwright. It includes functionality to click the "Download in Excel" button and optionally
save the file to a specific path, bypassing interactive file dialogs using Playwright's download handling.

Contents:
- download_report: clicks the download button and saves the file
"""

from pathlib import Path
import pandas as pd
from playwright.async_api import Page, Download
#from config.settings import data_folder, csv_filename

async def download_report(page: Page, save_path: str) -> Path:
    """
    Click the "Download in Excel" button and save the downloaded file to the specified path.

    INPUTS:
    - page: Playwright Page object. The page must have already generated a report table.
    - save_path: string. Full path (including filename) where the Excel file should be saved.

    OUTPUTS:
    - saved_file_path: Path object representing the saved Excel file.
    """

    # Ensure save path is a Path object
    save_file_path = Path(save_path)

    # Set up listener for download
    async with page.expect_download() as download_info:
        # Click the Download button
        await page.locator("input.btn.btn-info[value='Download in Excel']").click()

    download: Download = await download_info.value

    #Read in as csv and remove header row
    #format_downloaded_file(save_file_path)
    # Save file to specified location
    #saved_file_path = await download.save_as(str(save_file_path))
    await download.save_as(str(save_file_path))

    df = pd.read_csv(save_file_path, skiprows=1)  # Skip first row
    df.to_excel(save_file_path, engine='odf', index=False)  # Save back to CSV without index
    
    return df

    
