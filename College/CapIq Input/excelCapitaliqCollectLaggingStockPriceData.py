
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
from BasicCommandsKuliah import *


###################################################################

def main():
    bruteForceHausman()
    # collectLaggingStockPriceData()
    # ctrlS()
    
    pass

def collectLaggingStockPriceData():
    time.sleep(3)
    print("run")
    i = 0
    while i < 790:
        print("loop :",i)
        copyy()
        time.sleep(1)
        arrowRightt()
        time.sleep(0.3)
        pastee()
        
        i += 1

        if i % 30 == 0:
            print("preparing to print")
            ctrlS()
            print("saved")
            time.sleep(7)
        time.sleep(5)

variableListHausman = ["dz_w","esg_w","size_w","lev_w","slack_w","prof_w","liq_w","vola_w","ret_w","loss","div"]

def bruteForceHausman():
    time.sleep(2)
    
    i = 2

    j = 0 #utk fe
    k = 0 #utk fe

    m = 0 #utk re
    n = 0 #utk re

    while i < len(variableListHausman):
        while (i+k) < len(variableListHausman):
            # bagian fe
            write("xtreg ")
            while j < i:
                write(variableListHausman[j])
                write(" ")
                j+=1
            write(variableListHausman[i+k])
            j=0
            write(", fe")
            enterr()
            write("est store fe")
            enterr()
            
            #bagian re
            write("xtreg ")
            while m < i:
                write(variableListHausman[m])
                write(" ")
                m+=1
            write(variableListHausman[i+k])
            m=0
            write(", re")
            enterr()
            write("est store re")
            enterr()
            write("hausman fe re")
            enterr()
            k+=1
            a = input()
            print("put cursor back to stata terminal")
            time.sleep(2)
            # write("\n")

        i+=1
        j=0
        k=0
            
            

    pass

if __name__ == '__main__':
    main()