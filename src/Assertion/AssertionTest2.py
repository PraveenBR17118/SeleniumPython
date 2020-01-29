'''
Created on 23-Jan-2020

@author: praveen
'''
#assertTrue and assertFalse

import unittest
from selenium import webdriver

class Test1(unittest.TestCase):
    
    
    def testName(self):
        self.driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")
        self.driver.get("https://google.com")
        titleofWebpage=self.driver.title
        
        #assertTrue
        
        #self.assertTrue(titleofWebpage == "Google", "Titles of the web page are same")
        self.assertFalse(titleofWebpage == "Google", "Titles of the web page are same")
         
if __name__=="__main__":
    unittest.main()
