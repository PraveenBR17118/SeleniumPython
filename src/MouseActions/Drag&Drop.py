'''
Created on 21-Jan-2020

@author: praveen
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")

actions = ActionChains(driver)

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

driver.maximize_window()

rom_bttn = driver.find_element_by_xpath("//div[@id='box6']")

italy_button = driver.find_element_by_xpath("//div[@id='box106']")

actions.drag_and_drop(rom_bttn, italy_button).perform() # drag and drop 