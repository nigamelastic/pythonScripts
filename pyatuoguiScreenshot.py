import pyautogui, time
from PIL import ImageGrab
# pyautogui.displayMousePosition()

# p1  =   [661,130]
# p2  =   [1239,130]
# p3  =   [1239,973]
# p4  =   [661, 973]

time.sleep(6)
for i in range(10):
    im1 = pyautogui.screenshot(region=(661,130, 578, 843))
    PageNum= "Page"+str(i)
    im1.save(r'screenshots\\'+PageNum+r'.png')

    pyautogui.moveTo(1878, 992, 2)
    pyautogui.click(x=1878, y=992) 


    time.sleep(2)
      
     
    print(i)
    