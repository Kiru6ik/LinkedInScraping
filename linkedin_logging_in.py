# Getting necessary tools for our program.

from linkedin_scraper import Person, actions  # Tools for fetching LinkedIn data.
from selenium.webdriver.chrome.options import Options  # Allows us to set special settings for our browser.
from selenium import webdriver  # Tool that lets our program interact with a web browser.
from selenium.webdriver.chrome.service import Service as ChromeService  # Helps manage our Chrome browser.
from webdriver_manager.chrome import ChromeDriverManager  # Makes sure we get the latest version of the Chrome browser.

# Setting up specific settings for our browser.
options = Options()
options.add_argument("user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3")  # Pointing to a specific browser profile.

# Starting our web browser with the settings we've defined.
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# Pausing our script for a while.
import time

# Using our browser to visit LinkedIn's main page.
driver.get("https://www.linkedin.com/")
time.sleep(300)  # Pausing for 300 seconds, so you have time to interact with the page, login or do some tasks.
