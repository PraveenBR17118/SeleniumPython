'''
Created on 23-Jan-2020

@author: praveen
'''
import pytest
@pytest.yield_fixture()
def setup():
    print("Opening URL to Signup")
    yield 
    print("Closing browser after Signup")

def test_SignupByemail(setup):
    print("This is Login by email test")
    
def test_SignupByfacebook(setup):
    print("This is Login by facebook test")