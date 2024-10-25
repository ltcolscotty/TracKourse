"""V2 implementation serves to use playwright for faster scraping, and direct URL
searches to reduce instances of wrong results showing up"""


def get_search_url(subject, catalog_number, campus, session, term):
    """Gets filtered URL based on inputs
    Args:
        subject: str - Subject (eg. [MAT] xxx)
        catalog_number: str - catalog number (eg. xxx [101])
        campus: str - all caps campus location (eg. ICOURSE, TEMPE)
        session: str - A, B, or C
        term: str - 2251, broken down into (2xxx - default, x25x - year (eg 2025 -> x25x), xxx1 (Semester))

    Returns:
        str: URL to access
    """
    base_url = "https://catalog.apps.asu.edu/catalog/classes/classlist"
    # Construct the URL with the given parameters
    url = (
        f"{base_url}?campus={campus}&campusOrOnlineSelection=C&catalogNbr={catalog_number}"
        f"&honors=F&promod=F&searchType=open&session={session}&subject={subject}&term={term}"
    )
    return url


def scan_boxes(page):
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
