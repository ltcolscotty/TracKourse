from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

# Get the current directory (assuming your script is in the root of your repository)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the path to the driver folder
driver_path = os.path.join(current_dir, "driver")

# Use WebDriverManager to download and install ChromeDriver to the specified path
driver_manager = ChromeDriverManager(path=driver_path).install()

# Create a Service object with the installed driver path
service = Service(driver_manager)

# Create the WebDriver instance
driver = webdriver.Chrome(service=service)

