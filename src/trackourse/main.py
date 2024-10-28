import time

from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

import nonmodify.web_info as wi2
import nonmodify.process_classes as pc2
import nonmodify.alert_handler as alerter

import const_config as cc


def main():
    url_list = []
    previous_lists = []
    # puts url variables in scope for efficiency
    if cc.search_method == "class_list":
        for course in cc.class_list:
            url_list.append(
                wi2.get_search_url(
                    course.subj,
                    course.nbr,
                    course.location.upper(),
                    course.session,
                )
            )
        previous_lists = [[] for i in range(len(cc.class_list))]
    elif cc.search_method == "id_list":
        for id in cc.id_list:
            url_list.append(wi2.url_from_id(id))
        previous_lists = [[] for i in range(len(cc.id_list))]
    else:
        raise Exception("Invalid search method. Check const_config.py's search_method")

    with sync_playwright() as p:
        try:
            while True:
                browser = p.chromium.launch(headless=False, channel="chrome")
                page = browser.new_page()

                for index_url, url in enumerate(url_list):
                    max_retries = 3
                    retry_count = 0
                    while retry_count < max_retries:
                        try:
                            page.goto(url, timeout=30000)  # 30 seconds timeout

                            # Get information found
                            if wi2.found_results(page):
                                print(
                                    f"Log: Open results for {cc.class_list[index_url].fullcode}"
                                )
                                result_list = wi2.scan_boxes(page)
                                result_list = pc2.standardize(
                                    result_list, cc.class_list[index_url]
                                )

                                # Process each course
                                for index_course, course in enumerate(result_list):
                                    result_list[index_course] = pc2.process_class(
                                        course
                                    )

                                result_list = pc2.filter_info(
                                    result_list, cc.class_list[index_url]
                                )

                                new_classes = pc2.compare_results(
                                    previous_lists[index_url], result_list
                                )
                                previous_lists[index_url] = result_list

                                if new_classes is not None:
                                    alerter.send_alerts(new_classes)
                                else:
                                    print("No new status updates")
                            else:
                                print(
                                    f"Log: No open results for {cc.class_list[index_url].fullcode}"
                                )

                            break  # Exit the retry loop if successful

                        except PlaywrightTimeoutError:
                            retry_count += 1
                            print(
                                f"Timeout occurred for {cc.class_list[index_url].fullcode}. Retrying... (Attempt {retry_count}/{max_retries})"
                            )
                            time.sleep(10)  # Wait for 10 seconds before retrying

                    if retry_count == max_retries:
                        print(
                            f"Failed to load {cc.class_list[index_url].fullcode} after {max_retries} attempts. Skipping..."
                        )

                print(f"Waiting for {cc.wait_time} seconds before next check...")
                time.sleep(cc.wait_time)
                browser.close()

        except KeyboardInterrupt:
            print("\nProgram stopped by user")
        finally:
            if "browser" in locals():
                browser.close()


if __name__ == "__main__":
    main()
