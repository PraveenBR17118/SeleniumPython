'''
Created on 20-Jan-2020

@author: praveen
'''

from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")

driver.get("http://fs2.formsite.com/meherpavan/form2/index.html?1537702596407") 

Bst_dropdown = Select(driver.find_element_by_id("RESULT_RadioButton-9"))

# select by visible text
#Bst_dropdown.select_by_visible_text("Morning")

# select by index
#Bst_dropdown.select_by_index(2)

#select by value 
Bst_dropdown.select_by_value("Radio-2")

#Capture all the options and print them as output
all_options = Bst_dropdown.options

for i in all_options:
    print(i.text)

#count the number of options 
print(len(Bst_dropdown.options))