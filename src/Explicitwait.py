'''
Created on 20-Jan-2020

@author: praveen
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")

driver.implicitly_wait(5)

driver.maximize_window()

driver.get("http://www.expedia.com/") 

Flight_button=driver.find_element(By.ID,"tab-flight-tab-hp")

Flight_button.click()  # Click on flights button 

time.sleep(3)

#ffFlight = driver.find_element(By.ID,"package-origin-hp-package")

#ffFlight = driver.find_element_by_xpath("//input[@id='package-origin-hp-package']")

#ffFlight= driver.find_element_by_css_selector('from#loginFrom [id= "package-origin-hp-package"]')

#ffFlight = driver.find_element_by_xpath("//label[@for='package-origin-hp-package']")

#driver.execute_script("arguments[0].click();", ffFlight)

#ffFlight = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"package-origin-hp-package")))

ffFlight = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "//*[@data-typeahead='uTA-attached']")))

driver.execute_script("arguments[0].click();", ffFlight)

#ffFlight.click()

ffFlight.send_keys("SFO") # Origin

time.sleep(3)

ddFight = driver.find_element(By.ID,"package-destination-hp-package")

ddFight.send_keys("NYC") # Destination

time.sleep(3)

Dep_Cal = driver.find_element(By.ID,"package-departing-hp-package")

Dep_Cal.clear()

time.sleep(3)

Dep_Cal.send_keys("20/01/2020")

Ret_cal = driver.find_element(By.ID,"package-returning-hp-package")

Ret_cal.clear()

Ret_cal.send_keys("22/01/2020")

Srch =  driver.find_element(By.ID,"search-button-hp-package")

Srch.click()