from selenium import webdriver

# DEFINE DRIVER
driver = webdriver.Opera()

# ENTER WEBSITE
driver.get("http://wiby.me")

# FULL SCREEN MODE
driver.maximize_window()

# FIND THE BUTTEN ON THE WEBSITE THAT SAYS "SUPPRICE ME!"
driver.find_element_by_xpath(xpath="/html/body/form/div[5]/a").click()

