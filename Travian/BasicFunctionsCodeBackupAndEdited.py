from PIL import ImageGrab
import os
import time

import win32api, win32con

from PIL import ImageOps
from numpy import *

import keyboard


x_pad = 0
y_pad = 0

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

#Built in code
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

def dragMouse(cord):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print ('Drag.')

def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print (x,",", y)
    detectedCoordinate = x , y
    return detectedCoordinate


def randomize(Position):
    randomx = random.randint(Position[0], Position[2])
    print(randomx)
    randomy = random.randint(Position[1], Position[3])
    print(randomy)
    
    ChromeRefresh = randomx, randomy
    print(ChromeRefresh)

    return ChromeRefresh


def GGBValueTest():
    tempCoord = get_cords()
    RGBvalues = fullScreenGrab().getpixel(tempCoord)
    print(RGBvalues)
    totall = sum(RGBvalues)
    print(totall)
    return totall

test = -245, 154
def ahah():
    mousePos(test)
    leftClick()

#End of Built in code









"""
end
"""
