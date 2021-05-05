
#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



expectedSongName='Faded'

def mailnotification():
    print("emailing................")
    email = "<email1>" # the email where you sent the email
    password = "<password>"
    send_to_email = "<email1>,<email2>, <email3>, <email4>" # for whom
    subject = "The Song has just Started!!!! Start the RAdio"
    message = "<custom mesage>"

    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = send_to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()
    print('Mail Sent')

if __name__ == '__main__':
     
    opts = Options()
    opts.binary_location = "/usr/bin/chromium"
    opts.add_argument("--headless")
    opts.add_argument("--window-size=1920x1080")
    browser = webdriver.Chrome(options=opts)

    browser.get('https://energy.at/wien')
    
    assert "ENERGY" in browser.title
    acceptCookie = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cookiePopup"]/div/div[1]/div[1]/label')))
    acceptCookie.click()
    try:
        while True:
            songname = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@class="trackTitle"]')))
            
            if expectedSongName.lower() in songname.text.lower():
                print("Song Found")
                mailnotification()
                break
            
            browser.refresh()

    except TimeoutException:
            print("No element found")
    print("finished")
    browser.close()

