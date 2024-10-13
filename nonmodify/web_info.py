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
    try:
        # Wait for the class results to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "class-results"))
        )

        # Find the container with class information
        class_results = driver.find_element(By.ID, "class-results")

        # Find all class rows
        class_rows = class_results.find_elements(By.CLASS_NAME, "class-accordion")

        output_text = ""

        for row in class_rows:
            # Extract relevant information
            course_info = row.find_element(By.CLASS_NAME, "course").text
            number = row.find_element(By.CLASS_NAME, "number").text
            instructor = row.find_element(By.CLASS_NAME, "instructor").text
            days = row.find_element(By.CLASS_NAME, "days").text
            time_start = row.find_element(By.CLASS_NAME, "start").text
            time_end = row.find_element(By.CLASS_NAME, "end").text
            location = row.find_element(By.CLASS_NAME, "location").text
            seats = row.find_element(By.CLASS_NAME, "seats").text

            # Format the output
            output_text += f"{course_info}\n"
            output_text += f"{number}\n"
            output_text += f"{instructor}\n"
            output_text += f"{days} | {time_start} - {time_end}\n"
            output_text += f"{location}\n"
            output_text += f"{seats}\n"
            output_text += "\n"  # Add a blank line between classes

        return output_text

    except Exception as e:
        print(f"An error occurred: {e}")
        return ""


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
