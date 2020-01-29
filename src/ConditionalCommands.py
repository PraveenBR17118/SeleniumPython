'''
Created on 20-Jan-2020

@author: praveen
'''

from selenium import webdriver

#import selenium.webdriver.common.keys

driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")

driver.get("http://newtours.demoaut.com/")

print(driver.title) # Welcome: Mercury Tours

un = driver.find_element_by_xpath("//input[@name='userName']")

print(un.is_displayed() ) # boolean value 

print(un.is_enabled())  #returns eithwer true of false 

pwd = driver.find_element_by_xpath("//input[@name='password']")

print(pwd.is_displayed() ) # boolean value 

print(pwd.is_enabled())  #returns eithwer true of false 

lgn = driver.find_element_by_xpath("//input[@name='login']")
 
print(pwd.is_displayed() ) # boolean value 

print(pwd.is_enabled())

un.send_keys("mercury")

pwd.send_keys("mercury")

lgn.click()

roundtrip_radio = driver.find_element_by_css_selector("input[value=roundtrip]")

print(roundtrip_radio.is_selected()) # Print status of radio button

onevalue_radio = driver.find_element_by_css_selector("input[value=oneway]")

print(onevalue_radio.is_selected())

