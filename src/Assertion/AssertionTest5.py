'''
Created on 23-Jan-2020

@author: praveen
'''

#Relational Comparison 

import unittest

class Test(unittest.TestCase):
    def testName(self):
                #assertGreater
        #self.assertGreater(100, 10, "msg")  
            #assertGreaterEqual
        #self.assertGreaterEqual(100, 1001, "msg")  
                #assertLess
        #self.assertLess(10, 100, "msg")
        
                #assertLessEqual
        self.assertLessEqual(101, 100, "msg")
        
             
        
        
if __name__ =="__main__":
    unittest.main()