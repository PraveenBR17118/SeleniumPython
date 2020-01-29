'''
Created on 23-Jan-2020

@author: praveen
'''
import unittest

class SignupTest(unittest.TestCase):
    
    def test_SignupbyEmail(self):
        print("This is signup by email test")
        self.assertTrue(True)
        
    def test_SignupbyFacebook(self):
        print("This is signup by facebook test")
        self.assertTrue(True)
        
    def test_Signupbytwitter(self):
        print("This is signup by twitter test")
        self.assertTrue(True)
        
if __name__== "__main__":
    unittest.main()