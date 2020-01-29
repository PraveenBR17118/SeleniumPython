'''
Created on 22-Jan-2020

@author: praveen
'''

from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")

driver.get("https://www.amazon.in")

#capture all the cookies created by browser

cookies = driver.get_cookies()

print(len(cookies)) # print number of cookies have been created 

print(cookies) # print all the cookie present

#Adding new cookie to the browser 
cookie={'name':'Mycookie','value':'12345678999'}

driver.add_cookie(cookie)

cookies1 = driver.get_cookies()

print(len(cookies1)) # print number of cookies after adding new cookie 

print(cookies1) # print all the cookie present

#Deleting cookie 

driver.delete_cookie('Mycookie')

cookies2 = driver.get_cookies()

print(len(cookies2)) # print number of cookies after deletin new cookie 

print(cookies2) # print all the cookie present

#Deleting all the cookies 

driver.delete_all_cookies()

cookies2 = driver.get_cookies()

print(len(cookies2)) # print number of cookies after deletin all cookies

print(cookies2) # print all the cookie present
