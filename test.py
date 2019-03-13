from selenium.webdriver.chrome.webdriver import WebDriver
import time

wd = WebDriver()
wd.get("https://www.google.pl")
time.sleep(3)