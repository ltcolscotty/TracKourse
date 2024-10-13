import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def access_page(driver):
    """clear search bars and search the class input"""
    pass


def scan_boxes(driver):
    """Look through the page and scan through divs"""
    # Find all elements on the page
    all_elements = driver.find_elements(By.XPATH, "//*")
    # Print details of each element
    # REMOVE ONCE DONE WITH PROGRAMMING
    for element in all_elements:
        tag = element.tag_name
        element_id = element.get_attribute("id")
        element_class = element.get_attribute("class")
        text_content = element.text


def agg_data():
    """Process one box input into an analyzable dataform"""
    pass


def next_page(driver, timeout=10):
    """Iterate to next page if there is a next page"""
    try:
        # Wait for the class results to be present
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, "class-results"))
        )

        # Look for the pagination element
        pagination = driver.find_element(By.CLASS_NAME, "pagination")

        # Find all list items in the pagination
        pagination_items = pagination.find_elements(By.TAG_NAME, "li")

        # Check if there's a "Next" button
        next_button = None
        for item in pagination_items:
            if "next" in item.get_attribute("class"):
                next_button = item.find_element(By.TAG_NAME, "a")
                break

        if next_button and "disabled" not in next_button.get_attribute("class"):
            next_button.click()
            print("Clicked to the next page")
            return True
        else:
            print("Next page button not found or disabled. This may be the last page.")
            return False

    except TimeoutException:
        print("Class results not found within the timeout period.")
        return False
    except NoSuchElementException:
        print("Pagination element not found.")
        return False
