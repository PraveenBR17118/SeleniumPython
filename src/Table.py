'''
Created on 20-Jan-2020

@author: praveen
'''

from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")

driver.get("file:///Users/praveen/Documents/Eclipse%20Project/PythonAutomation/SeleniumPython/Sampl3.html")  # Count the number of rows

rows = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr"))

cloms = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th"))

print(rows)

print(cloms)


print("Product"+"   "+"Artcle"+"   "+"Price")   #/html/body/table/tbody/tr[2]/td[1]

for r in range(2,rows+1):
    for c in range(1,cloms+1):
        value=driver.find_elements_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]")[0].text
        print(value,end= "    ")
    print()
        