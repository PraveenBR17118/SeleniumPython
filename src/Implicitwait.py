'''
Created on 20-Jan-2020

@author: praveen
'''

from selenium import webdriver

#import selenium.webdriver.common.keys

driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")

driver.get("http://newtours.demoaut.com/") # opening URL take some time

#Wait for some time

driver.implicitly_wait(10) # wait for seconds

assert "Welcome: Mercury Tours" in driver.title 

un = driver.find_element_by_xpath("//input[@name='userName']")

pwd = driver.find_element_by_xpath("//input[@name='password']")

lgn = driver.find_element_by_xpath("//input[@name='login']")

un.send_keys("mercury")

pwd.send_keys("mercury")

lgn.click()
