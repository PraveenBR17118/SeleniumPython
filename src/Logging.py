'''
Created on 22-Jan-2020

@author: praveen
'''
import logging

path = "/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Log/"

logging.basicConfig(filename = path + "test.log",
                    format = '%(asctime)s: %(levelname)s: %(message)s',
                    datefmt = '%d/%m/%Y %I:%M:%s %p',
                    level = logging.DEBUG )


logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")