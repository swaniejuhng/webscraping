from selenium import webdriver

driver = webdriver.PhantomJS(executable_path = 'C:/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver.get("httpL//en.wikipedia.org/wiki/Monty_Python")
assert "Monty Python" in driver.title
print("Monty Python was not in the title")
driver.close()
