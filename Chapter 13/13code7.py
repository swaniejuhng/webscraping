from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains

# REPLACE WITH YOUR DRIVER PATH. EXAMPLES FOR CHROME AND PHANTOMJS
driver = webdriver.PhantomJS(executable_path = 'C:/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')
# driver = webdriver.Chrome(executable_path = '../chromedriver/chromedriver')

driver.implicitly_wait(5)
driver.get("http://pythonscraping.com/")
driver.get_screenshot_as_file("C:/WebScraping/tmp/pythonscraping.png")
