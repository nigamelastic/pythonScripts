import unittest
from selenium import webdriver
from initialPage import InitialPage

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--window-size=1920x1080")

        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        self.driver.get("yoururl like https://www.google.com")
        
        #username password mgmt
        self.username = input("Username:")
        self.password = getpass.getpass("Password for " + self.username + ":")
        self.fileLocation=input("file location: ")
        #config = configparser.ConfigParser()
        #config.read("happy.config")
        #self.password = config.get('JIRA', 'password')
        #self.username = config.get('JIRA', 'username')

    def test_search_in_python_org(self):
       
        p=excelworld(self.fileLocation)
        hosts=p.getAllHostNamesFromExcel()
        
        page = initialPage(self.driver)
        loginpage1 = Login(self.driver)
        loginpage1.loginUser(self.username,self.password)
        i=1
        pageDetails=[]
        
        time.sleep(3)
        while i<len(hosts):
            print(i)
            if(hosts[i].value != None):
                print(hosts[i].value)
                self.driver.refresh()
                self.driver.get('url')
                if(page.goToDetails(hosts[i].value)):
                    pageDetails.append(page.getpageDetails())
                    
                else:
                    pageDetails.append([self.notAvailableinpage,self.notAvailableinpage,self.notAvailableinpage])
            else:
                pageDetails.append(["NA","NA","NA"])
            
            i += 1
        p.saveAllpageDetails(pageDetails)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
