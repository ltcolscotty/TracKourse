from playwright.sync_api import sync_playwright

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
