'''
Created on 23-Jan-2020

@author: praveen
'''

import unittest

class PaymentTest(unittest.TestCase):
    
    
    def test_Paymentindollor(self):
        print("This is payment in dollor test")
        self.assertTrue(True)
        
    def test_paymentinRupees(self):
        print("This is payment in Rupees test")
        self.assertTrue(True)


if __name__== "__main__":
    unittest.main()