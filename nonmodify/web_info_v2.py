from playwright.sync_api import sync_playwright


def access_class_page(subject, catalog_number, campus, session):
    base_url = "https://catalog.apps.asu.edu/catalog/classes/classlist"
    # Construct the URL with the given parameters
    url = (
        f"{base_url}?campus={campus}&campusOrOnlineSelection=C&catalogNbr={catalog_number}"
        f"&honors=F&promod=F&searchType=open&session={session}&subject={subject}&term=2251"
    )

    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch()
        page = browser.new_page()

        # Navigate to the constructed URL
        page.goto(url)

        # Perform any additional actions if needed
        # For example: page.screenshot(path="screenshot.png")

        # Close the browser
        browser.close()


# Example usage
access_class_page("ENG", "102", "TEMPE", "C")
