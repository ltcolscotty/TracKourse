from playwright.sync_api import sync_playwright

import nonmodify.web_info_v2 as wi2
import const_config as cc

url_list = []

# puts url variables in scope for efficiency
for specification in cc.class_list:
    url_list.append(
        wi2.get_search_url(
            specification.subj,
            specification.nbr,
            specification.location.upper(),
            specification.session,
            cc.url_year,
        )
    )


with sync_playwright() as p:
    # Launch the browser
    browser = p.chromium.launch(headless=False, channel="chrome")
    page = browser.new_page()

    # Navigate to the constructed URL
    for url in url_list:
        page.goto(url)
        # do the scraping stuff

    # Perform any additional actions if needed
    # For example: page.screenshot(path="screenshot.png")

    # Close the browser
    browser.close()
