"""
Process:
- Initiate first search
Loop:
- Use scan and aggregate to find information
- Send Email if any Positives are found
- Clear results, next search starts
"""

import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException

from nonmodify.driver_installation_methods import get_chromedriver_path

import nonmodify.web_info as wi
import nonmodify.process_classes as aggregator

current_dir = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(current_dir, "driver")
chromedriver_path = get_chromedriver_path(driver_path)

with webdriver.Chrome(service=Service(chromedriver_path)) as driver:
    driver.get("https://catalog.apps.asu.edu/catalog/classes")
    driver.maximize_window()
    driver.implicitly_wait(10)

    try:
        wi.access_class(driver, "ENG", "102")
        string_result = wi.scan_boxes(driver)
        time.sleep(10)
        """if wi.wait_for_page_load(driver):
            if wi.next_page(driver):
                time.sleep(10)
                print("Page Toggler Success (1)")
            else:
                print("Page Toggler Fail (1)")
        else:
            print("Some issue occured")"""

        print(string_result)
        # print(aggregator.agg_data(string_result))

    except TimeoutException:
        print("Timed out waiting for page elements to load (Outer)")
