'''
Created on 23-Jan-2020

@author: praveen
'''
import pytest

@pytest.yield_fixture()
def setup():
    print("Opening URL to Login")
    yield 
    print("Closing browser after Login")

def test_loginByemail(setup):
    print("This is Login by email test")
    
def test_loginByfacebook(setup):
    print("This is Login by facebook test")