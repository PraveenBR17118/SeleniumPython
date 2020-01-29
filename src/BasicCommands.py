'''
Created on 17-Jan-2020

@author: praveen
'''
import time
from selenium import webdriver
#import selenium.webdriver.common.keys

# Chrome driver
driver = webdriver.Chrome(executable_path = "/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")

#driver = webdriver.Firefox(executable_path = "/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/geckodriver")

driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title) #return the Title of the page
print(driver.current_url) # return the URL of the page

driver.find_element_by_xpath("(//button[@class='btn btn-info'])[1]").click()

time.sleep(5) 

driver.close()
