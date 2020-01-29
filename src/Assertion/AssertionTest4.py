'''
Created on 23-Jan-2020

@author: praveen
'''
#assertIn and assertNotIn

import unittest

class Test4(unittest.TestCase):
    
    def testName(self):
        list1 = ("python","selenium","java")
        
        #self.assertIn("python",list1) #passed
        #self.assertIn("ruby",list1)  #failed
        
        #self.assertNotIn("python",list1) #passed
        self.assertNotIn("ruby",list1)#failed
        
        
        
        

if __name__ =="__main__":
    unittest.main()