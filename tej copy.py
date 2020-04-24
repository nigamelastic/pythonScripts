import requests
from lxml import html
import sys
import time


def getSlotDetails():
    headers1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
        'Content-Type': 'text/html',
    }
    result1=requests.get("https://www.waangoo.com/deliveryslotdetails",headers=headers1)
    
    doc = html.fromstring(result1.content)
    r=doc.xpath("//td")
    
    for slots in r:
        
        if(slots.get('class')=='disable'):
            print("Sorry no slots available")
            
        else:
            print("Slots Available ")
            sys.exit()
        

while True:
    getSlotDetails()
    time.sleep(3)
  