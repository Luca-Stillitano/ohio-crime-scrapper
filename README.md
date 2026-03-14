Ohio Crime Scraper
=================

Purpose
-------
This project is focused on scraping crime data for Ohio neighborhoods from the Ohio DPSO website. The functionality allows the user to automatically select report type, year, and time period, generate the crime report, and download the resulting data as an Excel file.

Project Structure
-----------------
```
ohio-crime-scraper/
│
├── config/
│   └── settings.py          # Global configuration and default values
│
├── data/
│   └── download/            # Directory to store downloaded Excel files
│
├── scraper/
│   ├── browser_actions.py   # Functions to launch browser and interact with dropdowns/buttons
│   ├── table_scraper.py     # Functions to scrape tables into structured data
│   └── download_actions.py  # Functions to handle downloading Excel reports
│
├── scripts/
│   ├── main.py              # Orchestrates scraping workflow (launch, select dropdowns, generate table, scrape/download)
│   └── setup_playwright.py  # Installs Playwright dependencies
│
└── requirements.txt         # Python dependencies
```

Setup Instructions
------------------

1. Clone the repository and navigate into it:
```bash
cd path/to/ohio-crime-scraper
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.\.venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install Playwright browsers and drivers:
```bash
python scripts/setup_playwright.py
```
Make sure to run this command from the root `ohio-crime-scraper` directory.

Running the Scraper
------------------

To test the scraping functionality (generating table and downloading report) run from the project root directory *\ohio-crime-scraper:
```bash
python -m scripts.main
```

The scraper will:
- Launch a visible browser window.
- Navigate to the Ohio DPSO crime report page.
- Select the configured dropdown options (report type, year, time period).
- Click 'Get Report' to generate the table.
- Download the resulting Excel report to the specified `data/download/` directory.

Configuration
-------------
- All default options (report type, year, time period, wait times, and browser headless option) are in `config/settings.py`.
- You can modify these values before running `main.py` to change the scraping behavior.

Fixes / Known Issues
-------------------
1. The downloaded Excel file may not save correctly to `data/download/` and could default to the `scripts/` directory.(Fixed as of 3/9/2026)
2. Currently, opening the downloaded Excel file may throw a formatting error; the file may not be properly structured. (Fixed as of 3/9/2026)

Next Steps
----------
- Fix the download path so files save correctly in `data/download/`.
- Ensure the Excel file is correctly formatted for direct opening.
- Extend scraping to other states or additional datasets.
- Build the neighborhood dashboard using this data as input.

