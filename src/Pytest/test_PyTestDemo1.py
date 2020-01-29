'''
Created on 23-Jan-2020

@author: praveen
'''

import pytest 

@pytest.fixture()
def setup():
    print("Once before every method")
    
def test_method1(setup):
    print("this is test method1")
    
def test_method2(setup):
    print("this is test method2")
    