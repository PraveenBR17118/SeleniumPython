'''
Created on 20-Jan-2020

@author: praveen
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")

driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")

driver.switch_to_frame("packageListFrame") #First Farame

driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()

time.sleep(3)

driver.switch_to_default_content()

driver.switch_to_frame("packageFrame") # Second Frame

driver.find_element(By.LINK_TEXT, "WebDriver").click()

time.sleep(3)

driver.switch_to_default_content()

driver.switch_to_frame("classFrame") # Third Frame

driver.find_element(By.LINK_TEXT,"Deprecated").click()