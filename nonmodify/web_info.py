import re
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    StaleElementReferenceException,
)


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

        print("class results loaded detected")

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


def agg_data(page_data):
    """Process box input into an analyzable dataform"""
    classes = []
    current_class = {}
    lines = page_data.strip().split("\n")

    for line in lines:
        line = line.strip()
        if not line:
            if current_class:
                classes.append(current_class)
                current_class = {}
            continue

        if line.isdigit():
            current_class["number"] = line
        elif "Syllabus" in line:
            current_class["has_syllabus"] = True
        elif "|" in line:
            days, times = line.split("|")
            current_class["days"] = days.strip()
            start, end = times.split("-")
            current_class["start_time"] = start.strip()
            current_class["end_time"] = end.strip()
        elif "open seats" in line.lower():
            seats = re.search(r"(\d+)\s+of\s+(\d+)", line)
            if seats:
                current_class["open_seats"] = int(seats.group(1))
                current_class["total_seats"] = int(seats.group(2))
        elif "ASU Online" in line:
            current_class["location"] = "ASU Online"
            current_class["days"] = "Online"
            current_class["start_time"] = "Online"
            current_class["end_time"] = "Online"
        elif "iCourse" in line:
            current_class["location"] = "iCourse"
            current_class["days"] = "iCourse"
            current_class["start_time"] = "iCourse"
            current_class["end_time"] = "iCourse"
        elif any(
            location in line
            for location in [
                "Tempe",
                "Poly",
                "Dtphx",
                "Calhc",
                "West Valley",
                "Los Angeles",
            ]
        ):
            current_class["location"] = line
        elif not current_class.get("instructor"):
            current_class["instructor"] = line

    if current_class:
        classes.append(current_class)

    # Post-processing to set 'Online' for classes without time information
    for class_info in classes:
        if "start_time" not in class_info or "end_time" not in class_info:
            class_info["days"] = class_info.get("days", "Online")
            class_info["start_time"] = "Online"
            class_info["end_time"] = "Online"

    return classes


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


def wait_for_page_load(driver, timeout=10):
    try:
        # Wait for the class results container to be present
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, "class-results"))
        )

        # Wait for at least one class result to be visible
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "class-accordion"))
        )

        """# Wait for the loading spinner to disappear
        WebDriverWait(driver, timeout).until_not(
            EC.presence_of_element_located((By.CLASS_NAME, "spinner-span"))
        )"""

        print("Page fully loaded!")
        return True

    except TimeoutException:
        print(f"Page did not load completely within {timeout} seconds")
        return False


def all_elements(driver, timeout=10, file_name="webpage_elements.txt"):
    try:
        if wait_for_page_load(driver, 10):

            # Find all elements on the page
            all_elements = driver.find_elements(By.XPATH, "//*")

            with open(file_name, "w", encoding="utf-8") as file:
                file.write(f"Total elements found: {len(all_elements)}\n\n")

                for index, element in enumerate(all_elements, start=1):
                    try:
                        tag_name = element.tag_name
                        element_id = element.get_attribute("id") or "N/A"
                        element_class = element.get_attribute("class") or "N/A"
                        element_text = element.text.replace("\n", " ")[
                            :50
                        ]  # Truncate long text

                        file.write(f"Element {index}:\n")
                        file.write(f"  Tag: {tag_name}\n")
                        file.write(f"  ID: {element_id}\n")
                        file.write(f"  Class: {element_class}\n")
                        file.write(f"  Text: {element_text}\n")
                        file.write("\n")
                    except StaleElementReferenceException:
                        file.write(f"Element {index}: Stale element, skipping\n\n")
                    except Exception as e:
                        file.write(f"Error processing element {index}: {str(e)}\n\n")

            print(f"Results have been saved to {file_name}")
        else:
            print("Page did not load properly")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
