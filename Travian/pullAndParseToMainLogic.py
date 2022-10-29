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

browserUrlCoord = 547,48
FirstTabChrome = 32,24
shellOfMainLogic = 1551,1000
###################################################################


def pullDataToBeParsed():
##    time.sleep(100)
##    click(browserUrlCoord)
    
    click(FirstTabChrome)
    selectAll()
    copyy()
    time.sleep(2)
    click(shellOfMainLogic)
    time.sleep(2)
    pastee()
    time.sleep(2)
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
