'''
Created on 23-Jan-2020

@author: praveen
'''

import unittest
from selenium import webdriver
from HtmlTestRunner.runner import HTMLTestRunner
#import HtmlTestRunner

class Test_OrangeHRM(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")
        cls.driver.maximize_window()
        
        
    def test_homepageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        #tit1 = self.driver.title
        #print(tit1)
        self.assertEqual("OrangeHRM", self.driver.title , "Web page title is not matching")
        
    def test_Login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        #tit2 = self.driver.title
        #print(tit2)
        self.assertEqual("OrangeHRM123", self.driver.title , "Web page title is not matching")
        
    @classmethod 
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Completed.......") 
        

if __name__ == "__main__":
    unittest.main(testRunner = HTMLTestRunner(output = "/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/HTMLReport"))
   
        