'''
Created on 22-Jan-2020

@author: praveen
'''
import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    
    def testName(self):
        self.driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")
        self.driver.get("https://www.google.com/")
        Titleofwebpage = self.driver.title
        #aasetEqual()
        
        #self.assertEqual("Google", Titleofwebpage,"Webpage title is not same ")
        self.assertNotEqual("Google123", Titleofwebpage, "Webpage title is not same")
        
if __name__ =="__main__":
    unittest.main()