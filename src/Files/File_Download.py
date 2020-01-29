'''
Created on 21-Jan-2020

@author: praveen
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()

#prefs = {"download.default_directory" : "/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Downloads/"}

chromeOptions.add_experimental_option("prefs", {"download.default_directory" : "/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Downloads/"})

driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver", chrome_options = chromeOptions)

driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()

#Download text file

txt_box1 = driver.find_element_by_id("textbox")

txt_box1.send_keys("testing download text file")

generate1 = driver.find_element_by_id("createTxt")

generate1.click()

dwnl1 = driver.find_element_by_id("link-to-download")

dwnl1.click()

pdf_box = driver.find_element_by_id("pdfbox")

pdf_box.send_keys("testing download pdf file")

generate2 = driver.find_element_by_id("createPdf")

generate2.click()

denl2 = driver.find_element_by_id("pdf-link-to-download")

denl2.click()

driver.close()

