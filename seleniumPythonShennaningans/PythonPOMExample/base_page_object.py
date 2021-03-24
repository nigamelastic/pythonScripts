from selenium import webdriver
from selenium.webdriver.common.by import By

 
class Page(object):
    """
    Base class that all page models can inherit from
    """
    def __init__(self, selenium_driver):
       
        self.driver = selenium_driver
        self.timeout = 30
 
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

 
  