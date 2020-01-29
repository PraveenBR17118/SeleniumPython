'''
Created on 21-Jan-2020

@author: praveen
'''

from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

driver.switch_to_frame(0)

upload_file = driver.find_element_by_xpath("//*[@id='RESULT_FileUpload-10']")

#driver.execute_script("arguments[0].scrollIntoView();",upload_file)

upload_file.send_keys("/Users/praveen/Documents/Nandi Pics/IMG_4833.jpg")