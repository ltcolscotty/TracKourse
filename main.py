import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from driver_installation_methods import get_chromedriver_path

current_dir = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(current_dir, "driver")
chromedriver_path = get_chromedriver_path(driver_path)

with webdriver.Chrome(service=Service(chromedriver_path)) as driver:
    driver.get("https://catalog.apps.asu.edu/catalog/classes")

    # Find all elements on the page
    all_elements = driver.find_elements(By.XPATH, "//*")
    # Print details of each element
    for element in all_elements:
        print(
            f"Tag: {element.tag_name}, ID: {element.get_attribute('id')}, Class: {element.get_attribute('class')}"
        )
