'''
Created on 20-Jan-2020

@author: praveen
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")

driver.get("http://newtours.demoaut.com/") 

links = driver.find_elements(By.TAG_NAME,"a")

print("Number of links present: ",len(links)) # Print how many links present in a page 

for i in links:
    print(i.text)
    
# How to click on the link

#driver.find_element(By.LINK_TEXT, "REGISTER").click()

driver.find_element(By.PARTIAL_LINK_TEXT, "REG").click()