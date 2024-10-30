"""V2 implementation serves to use playwright for faster scraping, and direct URL
searches to reduce instances of wrong results showing up"""

from playwright.sync_api import expect, Page
import trackourse.const_config as cc


def scan_boxes(page: Page):
    """Look through the page and scan through divs
    Args:
        page: Playwright Page
    Returns:
        str: formatted output text for aggregation function for one class
    """
    try:
        # Wait for the class results to be present
        page.wait_for_selector("#class-results")

        print("class results loaded detected")

        # Find the container with class information
        class_results = page.query_selector("#class-results")

        # Find all class rows
        class_rows = class_results.query_selector_all(".class-accordion")

        output_text = ""

        for row in class_rows:
            # Extract relevant information
            course_info = row.query_selector(".course").inner_text()
            number = row.query_selector(".number").inner_text()
            instructor = row.query_selector(".instructor").inner_text()
            days = row.query_selector(".days").inner_text()
            time_start = row.query_selector(".start").inner_text()
            time_end = row.query_selector(".end").inner_text()
            location = row.query_selector(".location").inner_text()
            seats = row.query_selector(".seats").inner_text()

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


def found_results(page: Page, timeout=5000):
    """Checks for if there are class results
    Args:
        page: playwright page
        timeout: timout time in ms

    Returns:
        bool: if results were found or not
    """
    class_results_div = page.locator("div.class-results")
    try:
        class_results_div.wait_for(state="attached", timeout=timeout)
    except TimeoutError:
        raise Exception("Timeout waiting for div.class-results to appear")

    no_classes_message = page.locator("div.class-results").get_by_text(
        "No classes found"
    )

    # Wait for either condition to be met
    result = page.wait_for_function(
        """
        () => {
            const accordions = document.querySelectorAll('div.class-results .class-accordion');
            const noClassesMessage = document.evaluate(
                "//div[contains(@class, 'class-results')]//text()[contains(., 'No classes found')]",
                document,
                null,
                XPathResult.FIRST_ORDERED_NODE_TYPE,
                null
            ).singleNodeValue;
            return {
                accordionsFound: accordions.length > 0,
                noClassesFound: !!noClassesMessage && noClassesMessage.isConnected
            };
        }
    """,
        timeout=timeout,
    )

    # Check which condition was met
    if result.evaluate("result => result.accordionsFound"):
        return True
    elif result.evaluate("result => result.noClassesFound"):
        print("No classes were found")
        expect(no_classes_message).to_be_visible()
        return False
    else:
        print(
            "Unexpected state: Neither class accordions nor 'No classes found' message were present"
        )
        return False


def url_from_id(id):
    """Gets the url based on searching by class ID
    Args:
        id: str - ID of class, 5 digit number

    Returns:
        url: str - URL to check results for
    """
    base_url = "https://catalog.apps.asu.edu/catalog/classes/classlist"
    url = f"{base_url}?campusOrOnlineSelection=C&honors=F&keywords=%20{id}&promod=F&searchType=open&term={cc.url_year}"
    return url
