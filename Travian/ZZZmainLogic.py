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

    

def AA():
    pullNewData()
    upgradeTimeLeft2()
    pass

def main():
##    setUpAndPositionShell()
##    build(1,sda0)
##    AA()

##    checkSDAAvailability(2,building0)
##    a3()
##    print(bob)
    time.sleep(5)
    parse()
    upgradeTimeLeft()

    pass
    
 
if __name__ == '__main__':
    main()



#end

