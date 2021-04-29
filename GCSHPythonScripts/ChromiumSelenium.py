from selenium import webdriver
from selenium.webdriver.chrome.options import Options
opts = Options()
opts.binary_location = "/usr/bin/chromium"
opts.add_argument("--headless")
opts.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=opts)
driver.get("https://www.google.com")

# capture the screen
driver.get_screenshot_as_file("capture.png")
