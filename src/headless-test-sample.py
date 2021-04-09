from package.selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')

with webdriver.Chrome(options=options) as chrome:
    chrome.get('https://google.com/')
    print(chrome.title)
    chrome.quit()