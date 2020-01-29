'''
Created on 20-Jan-2020

@author: praveen
'''
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")

driver.get("http://testautomationpractice.blogspot.com/") 

driver.find_element_by_xpath("//button[@onclick='myFunction()']").click()

time.sleep(5)

#driver.switch_to_alert().accept() # closes alert window using Ok button

driver.switch_to_alert().dismiss() # closses alert by using cancel  button 

