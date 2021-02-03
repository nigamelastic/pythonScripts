import configparser
import os
import shutil
from selenium.webdriver.common.action_chains import ActionChains
import sys
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
import openpyxl
from selenium.common.exceptions import NoSuchElementException 
import datetime
from dateutil.relativedelta import relativedelta  
from tika import parser

    
config = configparser.ConfigParser()
listOfShipperNumberVariables = ['Shipper reference','Shipment reference', 'Referenz Versender' ]
firefoxProfileName=r'default'
pdfDownloadFoldername = r'path to Downloads'
binary = r'firefox.exe'
OutDirectory = r'DHLPOD\\'
dhlPODMissingDirectory = r'DownloadDoesntExist'
options = Options()
options.set_headless(headless=False)
options.binary = binary
config.read("happy.config")
username = config.get('DHL','username')
password = config.get('DHL','password')

usernameInternal = config.get('DHLInternal','usernameInternal')
passwordInternal = config.get('DHLInternal','passwordInternal')

cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True 
fp = webdriver.FirefoxProfile(firefoxProfileName)

today = datetime.datetime.now().strftime("%d.%m.%Y")
twoMonthsBack = datetime.datetime.now() - relativedelta(months=2)
twoMonthBackFirstDay = twoMonthsBack.replace(day=1) 
twoMonthBackLastDay = twoMonthBackFirstDay + relativedelta(months=1) - relativedelta(days=1) 
print(twoMonthBackFirstDay.strftime("%d.%m.%Y"))
print(twoMonthBackLastDay.strftime("%d.%m.%Y"))
driver = webdriver.Firefox(fp, firefox_options=options,  capabilities=cap, executable_path="geckodriver.exe")
driver.get("https://www.ax4.com/ax4/control/man_dispatch_overview_shipper")
#driver.get("https://vendorcentral.amazon.de/hz/vendor/members/shipment-mgr/pendingasnselect")


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


driver.implicitly_wait(20)
driver.find_element_by_xpath('//*[@id="loginPage18"]/div/div[2]/form/input').send_keys(username)
driver.find_element_by_xpath('//*[@id="loginPage18"]/div/div[2]/form/div[2]/input').send_keys(password)
driver.find_element_by_xpath('//*[@id="loginPage18"]/div/div[2]/form/button').click()

driver.find_element_by_xpath('//*[@id="datefromval"]').send_keys(str(twoMonthBackFirstDay.strftime("%d.%m.%Y")))
driver.find_element_by_xpath('//*[@id="datetoval"]').send_keys(str(twoMonthBackLastDay.strftime("%d.%m.%Y")))
driver.find_element_by_xpath('//*[@id="main"]/div/table[2]/tbody/tr[2]/td/div[2]/div[2]/form[15]/div[2]/div[2]/div[1]/button').click()

#get the window handle after the window has opened
window_before = driver.window_handles[0]
time.sleep(2)
alleLinks = driver.find_elements_by_xpath('//*[@id="activeArea"]/table/tbody/tr/td[16]/a')
elemNo = 4
dhlPODmissing = open(dhlPODMissingDirectory+'\\'+today+'.txt','a+')
dhlPODmissing.write("Below are the Files That Couldn't be found today : \n") 
#checking all the links
for link in alleLinks:
    couldntFindshipperReference = driver.find_element_by_xpath('/html/body/div[1]/div/div/table[2]/tbody/tr[2]/td/div[2]/div[3]/form/div/span/table/tbody/tr['+str(elemNo)+']/td[6]').text
    link.click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    print(driver.title)
    driver.implicitly_wait(20)
    #this code will run only the first time
    if alleLinks.index(link) == 0:
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/ul/li[1]/a').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="actPageContentContainer"]/form/table/tbody/tr[2]/td[3]/input').send_keys(usernameInternal)
        driver.find_element_by_xpath('//*[@id="actPageContentContainer"]/form/table/tbody/tr[3]/td[3]/input').send_keys(passwordInternal)
        driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div[1]/div[2]/form/table/tbody/tr[5]/td[3]/input[1]').click()
        driver.find_element_by_xpath('//*[@id="shipmentSearchContainer"]/form[3]/table/tbody/tr[1]/td[3]/input[2]').click()
        time.sleep(1)

    downloadButton='/html/body/div[2]/div[4]/div[1]/div[1]/div[1]/div/a[2]/div'
    
    if check_exists_by_xpath(downloadButton):

        driver.find_element_by_xpath(downloadButton).click()
        for file in os.listdir(pdfDownloadFoldername):
            if '.pdf' in file:
                raw = parser.from_file(pdfDownloadFoldername+'\\'+file)
                contentText = raw['content']
                shipVarValue = r'Didnt find it'
                for listItem in listOfShipperNumberVariables:
                    if listItem in contentText:
                        shipVarValue=listItem
                print(shipVarValue)

                pdfSecondPart = contentText.split(shipVarValue, maxsplit=1)[-1]
                pdfTitleNewName = pdfSecondPart.split(maxsplit=2)[0]

                if pdfTitleNewName == "ASN":
                    pdfTitleNewName = pdfTitleNewName +'_'+ pdfSecondPart.split(maxsplit=2)[1]
                    print(pdfTitleNewName)
                else:
                    print(pdfTitleNewName)
                
                os.rename(pdfDownloadFoldername+'\\'+file,OutDirectory+pdfTitleNewName+'.pdf')
    else:
        print('The following shipper reference is missing : \n'+couldntFindshipperReference)
        dhlPODmissing.write(couldntFindshipperReference+'\n')

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    elemNo +=1



driver.quit()    

