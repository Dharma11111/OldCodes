from PIL import ImageGrab
import os
import time

import win32api, win32con

from PIL import ImageOps
from numpy import *

import keyboard

from more_itertools import locate
# from ZZZcollectData import *



rawData = ""
#input paste
def singleLineParse():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        if line == "=":
            break
        else:
            continue
    resultt = '\n'.join(lines)
    print(resultt)
    return resultt
    
    print("AAAAAAAAAAAAAAAAAA")
    print(resultt)
    print("AAAAAAAAAAAAAAAAAA")



def main():
    singleLineParse()
    pass
    
 
if __name__ == '__main__':
    main()

##rawData = singleLineParse()
##print (rawData)
##print (rawData.find("faster"))

#print (rawData[8])




#list_of_elems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test', 'Ok']
# Use more_itertools.locate() to find all indexes of an item 'Ok' in list

# index_pos_list = list(locate(rawData, lambda a: a == '\n'))
# print('Indexes of all occurrences of a "Ok" in the list are : ', index_pos_list)


#tes bisa dijumlah gak
##jam = rawData[rawData.find("faster")+7:rawData.find("faster")+8]
##menit = int(jam) * 60
##print (jam)
##print (menit)




#end