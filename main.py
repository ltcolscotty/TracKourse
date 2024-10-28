import time

from playwright.sync_api import sync_playwright

import nonmodify.web_info as wi2
import nonmodify.process_classes as pc2
import nonmodify.alert_handler as alerter

import const_config as cc


def main():
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

    previous_lists = [[] for i in range(len(cc.class_list))]

    with sync_playwright() as p:
        try:
            while True:
                browser = p.chromium.launch(headless=False, channel="chrome")
                page = browser.new_page()

                for index_url, url in enumerate(url_list):
                    page.goto(url)

                    # Get information found
                    if wi2.found_results(page):
                        print(
                            f"Log: Open results for {cc.class_list[index_url].fullcode}"
                        )
                        result_list = wi2.scan_boxes(page)
                        result_list = pc2.standardize(result_list)

                        # Process each course
                        for index_course, course in enumerate(result_list):
                            result_list[index_course] = pc2.process_class(course)

                        result_list = pc2.filter_info(
                            result_list, cc.class_list[index_url]
                        )

                        new_Classes = pc2.compare_results(
                            previous_lists[index_url], result_list
                        )

                        alerter.send_alerts(new_Classes)
                    else:
                        print(
                            f"Log: No open results for {cc.class_list[index_url].fullcode}"
                        )

                time.sleep(cc.wait_time)

        except KeyboardInterrupt:
            print("\nProgram stopped by user")
        finally:
            if "browser" in locals():
                browser.close()


if __name__ == "__main__":
    main()
