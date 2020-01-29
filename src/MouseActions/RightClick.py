'''
Created on 21-Jan-2020

@author: praveen
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")

driver.maximize_window()

rightclickbttn = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")

action = ActionChains(driver)

action.context_click(rightclickbttn).perform()
