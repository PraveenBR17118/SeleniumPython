'''
Created on 22-Jan-2020

@author: praveen
'''

import unittest

def setUpModule(): # will be executed before executing any class or any method present in the test class 
    print("Setup module outside class")


def tearDownModule(): # will be executed after completing everything present in the python module
    print("teardown module ")

class AppTesting(unittest.TestCase):
    
    @classmethod
    def setUp(self):
        print("This is login test")
        
    @classmethod
    def tearDown(self):  # Execute after each every test methods 
        print("This is logout")
        
    @classmethod
    def setUpClass(cls):  # Execute once when the class started 
        print("Opening application : Setupclass")

    @classmethod
    def tearDownClass(cls):  # Execute once after the class completed
        print("CLosing application : teardown class ")
    
    def test_search(self):
        print("This search test")

    def test_advancedsearch(self):
        print("This is Advanced search")

    def test_preparedRecharge(self):
        print("This is Prepared recharge test")

    def test_postpaidRecharge(self):
        print("This is Postpaid recharge test")
        
if __name__=="__main__":
    unittest.main()