from PIL import ImageGrab
import os
import time

import win32api, win32con

from PIL import ImageOps
from numpy import *

import keyboard


x_pad = 1088
y_pad = 381

FirstIncoming = 80,40
secondIncoming = -1023, 211

TempVariable = 75, 892 

LineIcon = -925, 320
LineSearchBar = -840, -325
ChatRoom = -888, -250
CallButton = 120, -325
VoiceCallButton = 120, -300
StartCallButton = -519, 2

ChromeRefreshRange = -1010, -335, -995, -325
alarmActive = -300, -170
alarmApp = -915, 315
currentTime = str(time.asctime( time.localtime(time.time()) ))
currentTimeCorrected = currentTime.replace(":","-")

"""
Zoom 90%
x_pad = 1088
y_pad = 381
TroopsMovement area = x_pad+1 , y_pad+1 , x_pad+288 , y_pad+165

FirstIncoming = 80,40
SecondIncoming = 80,70
"""

def screenGrab():
    time.sleep(2)
    b1 = (x_pad+1 , y_pad+1 , x_pad+288 , y_pad+165)
    im = ImageGrab.grab(b1)
    im.save(os.getcwd() + '\\full_snap__' + currentTimeCorrected + '.png', 'PNG')
    return im

def fullScreenGrab():
    time.sleep(2)
    b1 = (x_pad+1 , y_pad+1 , x_pad+288 , y_pad+165)
    im = ImageGrab.grab()
    im.save(os.getcwd() + '\\full_snap__' + currentTimeCorrected + '.png', 'PNG')
    return im

def WA():
    i = 1
    time.sleep(3)
    while i == 1:
        time.sleep(2)
        print('waiting1')

        time.sleep(random.randint(400,550))
        print('waiting2')
        
        mousePos(randomize())
        leftClick()
        time.sleep(2)
        print('waiting3')

        time.sleep(2)
        print('waiting4')

        if detect() == 212:
            time.sleep(2)
            print('waiting5')

            Alarm()

            break

def main():
    pass
    
 
if __name__ == '__main__':
    main()



def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print ('Click.')
    
def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print ('left Down')
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print ('left release')

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

#Cloningan tapi kekny salah
def mouseLOC(cord):
    win32api.SetCursorPos(cord)
    
def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print (x,",", y)
    detectedCoordinate = x , y
    return detectedCoordinate

def detect():
    RGBvalues = screenGrab().getpixel(FirstIncoming)
    print(RGBvalues)
    totall = sum(RGBvalues)
    print(totall)
    return totall

def randomize():
    randomx = random.randint(ChromeRefreshRange[0], ChromeRefreshRange[2])
    print(randomx)
    randomy = random.randint(ChromeRefreshRange[1], ChromeRefreshRange[3])
    print(randomy)
    
    ChromeRefresh = randomx, randomy
    print(ChromeRefresh)

    
    return ChromeRefresh


        


def Alarm():
    mousePos(alarmApp)
    leftClick()
    time.sleep(2)
    
    mousePos(alarmActive)
    leftClick()
    time.sleep(2)


def lineCall():
    print('Danger')
    mousePos(LineIcon)
    leftClick()
    time.sleep(2)
    mousePos(LineSearchBar)
    leftClick()
    time.sleep(2)
    keyboard.write('a.tes')
    time.sleep(2)
    mousePos(ChatRoom)
    leftClick()
    time.sleep(2)
    mousePos(CallButton)
    leftClick()
    time.sleep(2)
    mousePos(VoiceCallButton)
    leftClick()
    time.sleep(2)
    mousePos(StartCallButton)
    leftClick()
    time.sleep(2)
        
def GGBValueTest():
    tempCoord = get_cords()
    RGBvalues = fullScreenGrab().getpixel(tempCoord)
    print(RGBvalues)
    totall = sum(RGBvalues)
    print(totall)
    return totall

aa = -323, 148
bb = -465, -70
cc = -495, -8
dd = -501, 20
ee = -499, 48
ff = -480, 115
fff = -237, 55

gg = -635, 126

hh = -581, 128

ii = -671, 177
jj = -245, 154
kk = -705, -245

def ConstantRaid():
    i = 1
    time.sleep(300) 
    while i < 10:

        

        mousePos(aa)
        leftClick()
        time.sleep(4)
        mousePos(bb)
        leftClick()
        time.sleep(4)
        mousePos(cc)
        leftClick()
        time.sleep(4)
        mousePos(dd)
        leftClick()
        time.sleep(4)
        mousePos(ee)
        leftClick()
        time.sleep(4)
        mousePos(ff)
        leftClick()
        time.sleep(4)
        mousePos(fff)
        leftClick()
        time.sleep(4)
        mousePos(gg)
        leftClick()
        time.sleep(4)

        keyboard.write('67')
        leftClick()
        time.sleep(4)
    
        mousePos(hh)
        leftClick()
        time.sleep(4)
    
        keyboard.write('68')
        leftClick()
        time.sleep(4)

        mousePos(ii)
        leftClick()
        time.sleep(4)
        mousePos(jj)
        leftClick()
        time.sleep(4)
        mousePos(kk)
        leftClick()
        time.sleep(4)

        time.sleep(random.randint(1440, 1620))   

CheckAll = -670 , 109
StartRaid = -644, 191
def RaidMyself():
    i = 1
    time.sleep(1) 
    while i < 10:

        mousePos(CheckAll)
        leftClick()
        time.sleep(0.1)
        mousePos(StartRaid)
        leftClick()
        time.sleep(2)

"""
Notes:
LineIcon = -925, 320
LineSearchBar = -840, -325
ChatRoom = -888, -250
CallButton = 120, -325
VoiceCallButton = 120, -300
StartCallButton = -519, 2
"""
test = -245, 154
def ahah():
    mousePos(test)
    leftClick()

"""
end
"""
