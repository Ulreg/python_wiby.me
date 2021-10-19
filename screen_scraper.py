from selenium import webdriver

# DEFINE DRIVER
driver = webdriver.Opera()

# ENTER WEBSITE
driver.get("http://wiby.me")

# FULL SCREEN MODE
driver.maximize_window()

driver.find_element_by_xpath(xpath="/html/body/form/div[5]/a").click()

