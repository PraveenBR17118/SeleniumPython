'''
Created on 22-Jan-2020

@author: praveen
'''

import DataDriven.XLUtils
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")

driver.get("http://newtours.demoaut.com/")

driver.maximize_window()

driver.implicitly_wait(10)

path = "/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/DATA/DDT4.xlsx"

rows = DataDriven.XLUtils.getRowCount(path, "Sheet1")

for r in range(2,rows+1):
    username = DataDriven.XLUtils.readData(path, "Sheet1", r, 1)
    password = DataDriven.XLUtils.readData(path, "Sheet1", r, 2)
    
    driver.find_element_by_name("userName").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    
    driver.find_element_by_name("login").click()
    
    if driver.title=="Find a Flight: Mercury Tours: ":
        print("test is passed")
        DataDriven.XLUtils.writeData(path, "Sheet1", r, 3, "Test Passed")
    else :
        print("Test is failed")
        DataDriven.XLUtils.writeData(path, "Sheet1", r, 3, "Test Failed")
    
    driver.find_element_by_link_text("Home").click()
        