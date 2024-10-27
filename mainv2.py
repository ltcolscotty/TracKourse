import time

from playwright.sync_api import sync_playwright

import nonmodify.web_info_v2 as wi2
import nonmodify.process_classes_v2 as pc2
import const_config as cc

url_list = []

# puts url variables in scope for efficiency
for course in cc.class_list:
    url_list.append(
        wi2.get_search_url(
            course.subj,
            course.nbr,
            course.location.upper(),
            course.session,
            cc.url_year,
        )
    )


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, channel="chrome")
    page = browser.new_page()

    for index_url, url in enumerate(url_list):
        page.goto(url)

        # Get information found
        if wi2.found_results(page):
            print(f"Log: Open results for {cc.class_list[index_url].fullcode}")
            result_list = wi2.scan_boxes(page)
            result_list = pc2.standardize(result_list)

            # Process each course
            for index_course, course in enumerate(result_list):
                result_list[index_course] = pc2.process_class(course)

            result_list = pc2.filter_info(result_list, cc.class_list[index_url])
        else:
            print(f"Log: No open results for {cc.class_list[index_url].fullcode}")

    browser.close()
