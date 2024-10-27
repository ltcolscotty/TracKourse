from playwright.sync_api import sync_playwright

import nonmodify.web_info as wi2
import nonmodify.process_classes as pc2
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
    browser = p.chromium.launch(
        headless=False, channel="chrome", args=["--start-maximized"]
    )
    context = browser.new_context(no_viewport=True)
    page = context.new_page()

    input("Press Enter to close the browser...")

    # Close the browser
    browser.close()
