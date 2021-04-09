from package.selenium import webdriver
from package.selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

with webdriver.Remote(
    command_executor='http://hub:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME) as chrome:
    chrome.get('https://google.com/')
    time.sleep(3)
    print(chrome.title)
    chrome.quit()