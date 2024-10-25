from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import nonmodify.driver_installation_methods as dim

chromedriver_path = dim.setup_chromedriver()

# Create a Service object with the installed driver path
service = Service(chromedriver_path)

# Use the 'with' statement to create and manage the WebDriver instance
with webdriver.Chrome(service=service) as driver:
    driver.get("https://www.asu.edu")
    assert "ASU Homepage" in driver.title, "Unexpected page title"

print("Browser session completed and closed. Test successful.")
