'''
Created on 22-Jan-2020

@author: praveen
'''

import unittest

class Apptesting(unittest.TestCase):
    
    @unittest.SkipTest  #decorator
    def test_search(self):
        print("This is search test")
        
    @unittest.skip("I am skipping this test method because it is not yet ready")
    def test_advancedsearch(self):
        print("This advanced search method")
        
    @unittest.skipIf(1==1, "This method executes only if the condition is true")
    def test_preparedRecharge(self):
        print("This is prepared recharge test")
        
    def test_postpaidRecharge(self):
        print("This is postpaid recharge test")
        
    def test_loginbygmail(self):
        print("login by gmail")

    def test_loginbytwitter(self):
        print("login by twitter")
 
if __name__== "__main__":
    unittest.main()