'''
Created on 20-Jan-2020

@author: praveen
'''

from selenium import webdriver
#from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")

driver.get("http://demo.automationtesting.in/Windows.html")

clk_bttn = driver.find_element_by_xpath("//*[@id='Tabbed']/a/button")

clk_bttn.click()

print(driver.current_window_handle) # CDwindow-145142EEAB3EBE247B5EE1CAD54424AB

handles = driver.window_handles # return all the handle values of opened browser window 

for i in handles:
    driver.switch_to.window(i)
    print(driver.title)
    
    if driver.title == "Frames & windows":
        time.sleep(5)
        driver.close()
    
  
time.sleep(5)  
driver.quit()