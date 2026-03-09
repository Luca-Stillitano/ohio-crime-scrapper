# Author: Taaj Stillitano
# Email: Stillitano.engineering@gmail.com
# Date Created: 1/26/2026
# Date Last Updated: 1/26/2026

"""
Purpose:
This file contains functions for browser interactions using Playwright. 
It includes opening a browser, navigating to the site, selecting dropdown options,
clicking buttons (like 'Get Report'), and returning the page object for further scraping.

All browser actions are isolated here to make the scraper modular and maintainable.
"""

from playwright.async_api import Page
from config.settings import base_url, report_type, year, time_period, headless, page_load_wait, post_action_wait, table_generation_wait


async def launch_browser(p) -> tuple:
    """
    Launch a Chromium browser and open a new page to the base URL.

    INPUTS:
    - p: Playwright object from async_playwright() context

    OUTPUTS:
    - page: Playwright Page object, ready for interactions
    - browser: Browser instance (so it can be closed later)
    """
    browser = await p.chromium.launch(headless=headless)
    page = await browser.new_page()
    await page.goto(base_url)
    await page.wait_for_timeout(page_load_wait)
    return page, browser

async def select_dropdown_options(page: Page) -> None:
    """
    Select the configured dropdown options on the Ohio crime data page:
    report type, year, and time period.

    INPUTS:
    - page: Playwright Page object to interact with the website

    OUTPUTS:
    - None (modifies the page by selecting dropdowns)
    """
    # -----------------------------
    # 1. Report Type
    # -----------------------------
    await page.click("span.multiselect-selected-text")
    option = page.locator("ul.multiselect-container li").filter(
        has_text=report_type
    )
    await option.click()
    await page.wait_for_timeout(post_action_wait)

    # -----------------------------
    # 2. Year
    # -----------------------------
    await page.locator("button.multiselect.dropdown-toggle").filter(has_text="2025").click()
    await page.locator("ul.multiselect-container li label.radio").filter(has_text=year).click()
    await page.wait_for_timeout(post_action_wait)

    # -----------------------------
    # 3. Time Period
    # -----------------------------
    await page.locator("button.multiselect.dropdown-toggle").filter(has_text="FULL YEAR").click()
    await page.locator("ul.multiselect-container li label.radio").filter(has_text=time_period).click()
    await page.wait_for_timeout(post_action_wait)

async def click_get_report(page: Page) -> None:
    """
    Click the 'Get Report' button and wait for the table to generate.

    INPUTS:
    - page: Playwright Page object where the table will be generated

    OUTPUTS:
    - None (modifies the page by generating the table)
    """
    await page.locator("input.btn.btn-primary[value='Get Report']").click()
    await page.wait_for_timeout(table_generation_wait)

