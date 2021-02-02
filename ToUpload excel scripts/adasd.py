import sys
import os
import datetime
import xlrd
from selenium.common.exceptions import *
import configparser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
import openpyxl

foldername = r'path to folder multiExcel'
binary = r'path to firefox.exe'
options = Options()
options.set_headless(headless=False)
options.binary = binary



src =r'path to.xlsx'

cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True 
fp = webdriver.FirefoxProfile(r'default')

driver = webdriver.Firefox(fp, firefox_options=options,  capabilities=cap, executable_path="geckodriver.exe")
driver.implicitly_wait(20)



driver.get("https://vendorcentral.amazon.de/hz/vendor/members/shipment-mgr/summary?asn=16881211143")    
driver.find_element_by_xpath('//*[@id="displayShipmentButtons"]/div[1]/section[2]/span/kat-link/a').click()
driver.find_element_by_xpath('//*[@id="print-label-modal-span"]/kat-button/button').click()

driver.switch_to.window(driver.window_handles[1])
driver.get('https://www.google.com')
time.sleep(3)
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.get('https://yahoo.com')
time.sleep(60) 





















