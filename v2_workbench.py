from playwright.sync_api import sync_playwright

import nonmodify.web_info_v2 as wi2
import nonmodify.logger_helper as lh
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
    url = url_list[1]
    page.goto(url)

    result = wi2.scan_boxes(page)
    lh.write_file("v2test.txt", result)

    # Close the browser
    browser.close()
