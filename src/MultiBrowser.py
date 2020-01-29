'''
Created on 17-Jan-2020

@author: praveen
'''
from selenium import webdriver
#import selenium.webdriver.common.keys
#import org.openqa.selenium.WebDriver.common.keys

"""
from selenium import webdriver
#from selenium.webdriver.common.keys import keys


"""

#driver = webdriver.Chrome(executable_path = "/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")

driver = webdriver.Firefox(executable_path = "/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/geckodriver")
 
driver.get("http://newtours.demoaut.com/")

print(driver.title)

driver.quit()

