'''
Created on 20-Jan-2020

@author: praveen
'''
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")

driver.get("http://fs2.formsite.com/meherpavan/form2/index.html?1537702596407") 

# Working with radio buttons 

male_bttn = driver.find_element_by_id("RESULT_RadioButton-7_0")

print(male_bttn.is_selected())

driver.execute_script("arguments[0].click();", male_bttn)

print(male_bttn.is_selected())

#Working with Check Boxes
sun_chbox = driver.find_element_by_id("RESULT_CheckBox-8_0")

driver.execute_script("arguments[0].click();", sun_chbox)

sat_chbox = driver.find_element_by_id("RESULT_CheckBox-8_6")

driver.execute_script("arguments[0].click();", sat_chbox)

