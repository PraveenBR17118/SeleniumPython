'''
Created on 21-Jan-2020

@author: praveen
'''
from selenium import webdriver

fp = webdriver.FirefoxProfile()

fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf") #Mine type

fp.set_preference("browser.download.manager.showWhenStarting", False)

fp.set_preference("browser.download.dir", "/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Downloads/")

fp.set_preference("browser.download.folderList", 2)

fp.set_preference("pdfjs.disabled", True)

driver = webdriver.Firefox(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/geckodriver",
                           firefox_profile = fp)

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
