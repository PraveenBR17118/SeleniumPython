'''
Created on 22-Jan-2020

@author: praveen
'''

from selenium import webdriver

path = "/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Screenshot/"

driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")

driver.get("https://www.amazon.in")

driver.get_screenshot_as_file(path + "hompag.jpg")


#driver.save_screenshot(path+"homepage.png")