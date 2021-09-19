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
##from ZZZcollectData import *
##from ZZZvariablesDataSDAupgrade import *
##from ZZZmainLogic import queueList
##import ZZZmainLogic
###################################################################





def pullDataToBeParsed():
    shellOfMainLogic = [1173, 15]
    click(FirstTabChrome)
    selectAll()
    copyy()
    time.sleep(2)
    click(shellOfMainLogic)
    pastee()
    time.sleep(1)
    enterr()
    keyboard.type("=")
    enterr()
    pass

def main():
    pullDataToBeParsed()
    pass
    
 
if __name__ == '__main__':
    main()



#end

