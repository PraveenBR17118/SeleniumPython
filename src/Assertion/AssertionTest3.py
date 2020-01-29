'''
Created on 23-Jan-2020

@author: praveen
'''

#assertIsNone and assertIsNotNone

import unittest
from selenium import webdriver

class test1(unittest.TestCase):
    
    def testNmae(self):
        driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")
        
        #assertIsNone
        #self.assertIsNone(driver, "Driver is initiated")
        self.assertIsNotNone(driver, "Driver is not initiated")
        
        
if __name__ =="__main__":
    unittest.main()
