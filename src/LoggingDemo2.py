'''
Created on 22-Jan-2020

@author: praveen
'''
import logging

path = "/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Log/"

logging.basicConfig(filename = path + "test.log",
                    format = '%(asctime)s: %(levelname)s: %(message)s',
                    datefmt = '%d/%m/%Y %I:%M:%s %p' )

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)


logger.debug("This is a debug message")
logger.info("This is a info message")
logger.warning("This is a warning message")
logger.error("This is a error message")
logger.critical("This is a critical message")