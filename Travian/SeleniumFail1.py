from __future__ import print_function
from PIL import ImageGrab
import os
import datetime
import time

import win32api, win32con

from PIL import ImageOps
from numpy import *

import keyboard
from pynput.keyboard import Key, Controller
keyboard = Controller()

from more_itertools import locate

###################################################################
from BasicCommands import *
from ZZZcollectData import *
from ZZZvariablesDataSDAupgrade import *
###################################################################

def customCommand():
    time.sleep(0.5)
    keyboard.press(Key.f2)
    keyboard.release(Key.f2)
    ctrlLeftt()
    ctrlLeftt()
    ctrlLeftt()
    #time.sleep(0.5)
    keyboard.press(Key.f4)
    keyboard.release(Key.f4)
    #time.sleep(0.5)
    quitEditCell()

def main():
    time.sleep(2)
    i = 0
    while i < 250:
        
        customCommand()
        arrowDownn()
        time.sleep(0.5)
        i = i + 1
    pass
    
 
if __name__ == '__main__':
    main()



#end

