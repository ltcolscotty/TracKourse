import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from nonmodify.driver_installation_methods import get_chromedriver_path

current_dir = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(current_dir, "driver")
chromedriver_path = get_chromedriver_path(driver_path)

with webdriver.Chrome(service=Service(chromedriver_path)) as driver:
    driver.get("https://catalog.apps.asu.edu/catalog/classes")
    driver.implicitly_wait(10)

    try:
        # Wait for and interact with the catalog number input
        input_number_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "catalogNbr"))
        )
        input_number_element.clear()
        input_number_element.send_keys("267")

        # Wait for and interact with the subject input
        input_class_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "input[name='subject'][placeholder='Subject']")
            )
        )
        input_class_element.clear()
        input_class_element.send_keys("MAT")

        # Wait for the search button to be clickable
        search_button_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "search-button"))
        )
        search_button_element.click()

        # Wait for search results to load (adjust the condition as needed)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search-results"))
        )

    except TimeoutException:
        print("Timed out waiting for page elements to load")

    # Find all elements on the page
    all_elements = driver.find_elements(By.XPATH, "//*")
    # Print details of each element
    for element in all_elements:
        print(
            f"Tag: {element.tag_name}, ID: {element.get_attribute('id')}, Class: {element.get_attribute('class')}"
        )
