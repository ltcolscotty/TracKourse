import time

from playwright.sync_api import sync_playwright

import nonmodify.web_info_v2 as wi2
import nonmodify.process_classes_v2 as pc2
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
    for index, url in enumerate(url_list):
        page.goto(url)

        # Get information found
        result_list = wi2.scan_boxes(page)
        result_list = pc2.standardize(result_list)

        # Process each course
        for index, course in enumerate(result_list):
            result_list[index] = pc2.process_class(course)

        result_list = pc2.filter_info(result_list, cc.class_list[index])

    browser.close()
