'''
Created on 20-Jan-2020

@author: praveen
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")

driver.get("http://fs2.formsite.com/meherpavan/form2/index.html?1537702596407") 

Input_boxes = driver.find_elements(By.CLASS_NAME, 'text_field')

print(len(Input_boxes))

# How to provide the values to text box

first_name = driver.find_element_by_xpath("//*[@id='RESULT_TextField-1']")

first_name.send_keys("Praveen")

last_name = driver.find_element_by_xpath("//*[@id='RESULT_TextField-2']")

last_name.send_keys("B R")

last_name = driver.find_element_by_xpath("//*[@id='RESULT_TextField-3']")

last_name.send_keys("9090909090")