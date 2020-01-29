'''
Created on 23-Jan-2020

@author: praveen
'''
import unittest

from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignupTest

from Package2.TC_PayementTest import PaymentTest
from Package2.TC_PaymentReturnsTest import PaymentReturnsTest


#Get all the test from LoginTest,SignupTest,PaymentTest and PaymentReturnTest

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

#Creating test suites
sanityTestSuite = unittest.TestSuite([tc1,tc2])
functionalTestSuite = unittest.TestSuite([tc3,tc4])
masterTestSuite = unittest.TestSuite([tc1,tc2,tc3,tc4])

#unittest.TextTestRunner().run(sanityTestSuite)
#unittest.TextTestRunner().run(functionalTestSuite)
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)