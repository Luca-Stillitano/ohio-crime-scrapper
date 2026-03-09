from playwright.sync_api import sync_playwright
import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "playwright", "install"])