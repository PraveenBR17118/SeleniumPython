'''
Created on 21-Jan-2020

@author: praveen
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")

driver.get("http://opensource-demo.orangehrmlive.com")

Usr = driver.find_element_by_id("txtUsername")

pwd = driver.find_element_by_id("txtPassword")

lgn = driver.find_element_by_id("btnLogin")

Usr.send_keys("admin")

pwd.send_keys("admin123")

lgn.click()

admin = driver.find_element_by_xpath("//a[@id='menu_admin_viewAdminModule']")

usr_mang = driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")

usr = driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")

actions = ActionChains(driver)

actions.move_to_element(admin).move_to_element(usr_mang).move_to_element(usr).click(usr).perform()

