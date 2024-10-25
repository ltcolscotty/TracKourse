from playwright.sync_api import sync_playwright

from nonmodify.class_info import class_info as ci
import nonmodify.web_info_v2 as wi2
import const_config as cc

url_list = []
# Example access_class_page("MAT", "267", "TEMPE", "C", 2251)
for specification in cc.class_list:
    url_list.append(
        wi2.get_search_url(
            specification.subj,
            specification.nbr,
            specification.location.upper(),
        )
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
