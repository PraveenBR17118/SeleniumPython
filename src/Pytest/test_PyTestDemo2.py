'''
Created on 23-Jan-2020

@author: praveen
'''


import pytest

@pytest.yield_fixture()
def setup():
    print("Once before every method")
    yield
    print("Once after every method")
    
def test_method1(setup):
    print("This is test method1")
    
def test_method2(setup):
    print("This is test method2")