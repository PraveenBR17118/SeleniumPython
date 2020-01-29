'''
Created on 22-Jan-2020

@author: praveen
'''
import unittest
from selenium import webdriver
import time

class SearchEngineTest(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")
        self.driver.get("https://www.google.com/")
        time.sleep(5)
        print("Title of the page is : "+ self.driver.title) 
        self.driver.close()
        
    
    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")
        self.driver.get("https://bing.com/")
        time.sleep(5)
        print("Title of the page is : "+ self.driver.title)
        self.driver.close() 
        
if __name__=="__main__":
    unittest.main()