'''
Created on 21-Jan-2020

@author: praveen
'''

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window() #Maximize the window 

driver.implicitly_wait(5)

time.sleep(4)

# 1. scroll down page by pixel

#driver.execute_script("window.scrollBy(0,500)","")

# 2. scroll down page till the element found

#Element = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")

#driver.execute_script("arguments[0].scrollIntoView();",Element)

# 3. scroll down page till the end

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")