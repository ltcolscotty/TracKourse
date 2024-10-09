import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from driver_installation import get_chromedriver_path

current_dir = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(current_dir, "driver")
chromedriver_path = get_chromedriver_path(driver_path)

with webdriver.Chrome(service=Service(chromedriver_path)) as driver:
    driver.get("https://www.asu.edu")
    assert "ASU Homepage" in driver.title, "Unexpected page title"
