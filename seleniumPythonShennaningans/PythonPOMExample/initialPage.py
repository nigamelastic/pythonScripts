from selenium import webdriver
from selenium.webdriver.common.by import By
from base_page_object import Page
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class InitialPage(Page):
   
    #Locators
    hostNameSearchBar = (By.XPATH, '//*[@id="mainGrid"]/div/div[5]/div[2]/table/tbody/tr[2]/td[4]/div/div[2]/div/div/div[1]/input')
    detailsButton = (By.XPATH,'//*[@id="mainGrid"]/div/div[6]/div[2]/table/tbody/tr[1]/td[2]/div')
    delay=20
    pageTab=(By.XPATH,'/html/body/div[3]/div/div[2]/dx-scroll-view/div[1]/div/div[1]/div[2]/div/dx-form/div/div/div/div[6]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/span')
    arrayTeamsEngg=(By.XPATH,'/html/body/div[3]/div/div[2]/dx-scroll-view/div[1]/div/div[1]/div[2]/div/dx-form/div/div/div/div[6]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/dx-data-grid/div/div[6]/div/div/div[1]/div/table/tbody/tr/td[2]')
    arrayTeamsOperations=(By.XPATH,'/html/body/div[3]/div/div[2]/dx-scroll-view/div[1]/div/div[1]/div[2]/div/dx-form/div/div/div/div[6]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/dx-data-grid/div/div[6]/div/div/div[1]/div/table/tbody/tr/td[3]')
    arrayTeamspageEnv=(By.XPATH,'/html/body/div[3]/div/div[2]/dx-scroll-view/div[1]/div/div[1]/div[2]/div/dx-form/div/div/div/div[6]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/dx-data-grid/div/div[6]/div/div/div[1]/div/table/tbody/tr/td[1]')
    
    #Functions
    
    #go to the details Page
    def goToDetails(self,hostName):
        try:
            myElem = WebDriverWait(self, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mainGrid"]/div/div[5]/div[2]/table/tbody/tr[2]/td[4]/div/div[2]/div/div/div[1]/input')))
            #myElem.clear()
            #myElem.send_Keys(hostName)
            self.find_element(*self.hostNameSearchBar).clear()
            self.find_element(*self.hostNameSearchBar).send_keys(hostName)
            time.sleep(3)
            myElemDetails = WebDriverWait(self, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mainGrid"]/div/div[6]/div[2]/table/tbody/tr[1]/td[2]/div')))
            #myElemDetails.click()
            self.find_element(*self.detailsButton).click()
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            return False

        return True

        '''self.find_element(*self.hostNameSearchBar).clear()
        self.find_element(*self.hostNameSearchBar).send_keys(hostName)
        self.find_element(*self.detailsButton).click()'''

    #get the page details
    def getpageDetails(self):
        pageTabbutton = WebDriverWait(self, 20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div[2]/dx-scroll-view/div[1]/div/div[1]/div[2]/div/dx-form/div/div/div/div[6]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]')))
        time.sleep(3)
        self.find_element(*self.pageTab).click()
        time.sleep(3)
        arrayElemsEngg =self.driver.find_elements(*self.arrayTeamsEngg)
        allEnggTeamString=','.join(x.get_attribute('innerHTML') for x in arrayElemsEngg if x.get_attribute('innerHTML').strip())
        arrayElemsOps=self.driver.find_elements(*self.arrayTeamsOperations)
        allOpsTeamString=','.join(x.get_attribute('innerHTML') for x in arrayElemsOps if x.get_attribute('innerHTML').strip())
        arrayElemspageEnv=self.driver.find_elements(*self.arrayTeamspageEnv)
        allpageEnvString=','.join(x.get_attribute('innerHTML') for x in arrayElemspageEnv if x.get_attribute('innerHTML').strip())
     
        return pageDetailsList



class Login(Page):

    #Locators
    loginUsername=(By.ID,'input-username')
    loginPassword=(By.ID,'input-password')
    submitButton=(By.XPATH,'/html/body/ngx-app/ngx-auth/nb-layout/div/div/div/div/div/nb-layout-column/nb-card/nb-card-body/div/ngx-login/div/div/nb-card/nb-card-body/nb-auth-block/form/button')


    def loginUser(self,usernameString,passwordString):
        self.find_element(*self.loginUsername).send_keys(usernameString)
        self.find_element(*self.loginPassword).send_keys(passwordString)
        self.find_element(*self.submitButton).click()

