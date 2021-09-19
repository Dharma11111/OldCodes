from BasicCommands import *
from AutoFarmNewServerFarmListOnly import *
from PIL import ImageGrab
import os
import time

import win32api, win32con

from PIL import ImageOps
from numpy import *

import keyboard

from more_itertools import locate
from ZZZcollectData import *



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
    # print(resultt)
    return resultt
    
    print("AAAAAAAAAAAAAAAAAA")
    print(resultt)
    print("AAAAAAAAAAAAAAAAAA")

def coordIndex():
    rawData = singleLineParse()
    startingPointLoop = 0
    # print("...",len(rawData))
    Xcoord = []
    Ycoord = []
    XYCoordIndex = 0
    while startingPointLoop < len(rawData):
        
        indexesOpenBracket = rawData.find("(",startingPointLoop)
        indexesSeparator = rawData.find("|",startingPointLoop)
        indexesCloseBracket = rawData.find(")",startingPointLoop)
        if indexesOpenBracket == -1:
            break
        
        print(indexesOpenBracket)
        print(rawData[indexesOpenBracket])
        print(indexesSeparator)
        print(rawData[indexesSeparator])
        print(indexesCloseBracket)
        print(rawData[indexesCloseBracket])
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        startingPointLoop = indexesCloseBracket + 1
        Xcoord.append(rawData[ indexesOpenBracket+1 : indexesSeparator ])
        Ycoord.append(rawData[ indexesSeparator+1   : indexesCloseBracket])
        print(Xcoord)
        print(Ycoord)
        # time.sleep(5)
    # print(rawData)
    print(len(Xcoord))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(len(Ycoord))
    # collectedCoordAmount = len(Xcoord)
    # i = 0
    # while i < collectedCoordAmount:
    #     print


XX = ['57', '58', '65', '63', '78', '79', '68', '76', '22', '82', '79', '81', '33', '53', '73', '72', '83', '57', '93', '20', '87', '93', '75', '68', '91', '43', '74', '24', '62', '22', '64', '21', '43', '107', '111', '58', '91', '5', '111', '11', '116', '37', '116', '115', '113', '116', '48', '118', '15', '116']
YY = ['1', '2', '-8', '18', '0', '16', '27', '21', '10', '20', '24', '-20', '-31', '41', '37', '38', '30', '45', '20', '-29', '33', '29', '45', '-48', '36', '52', '50', '46', '54', '45', '54', '45', '-54', '19', '-5', '60', '-45', '38', '-17', '46', '-1', '62', '-7', '-13', '-20', '-10', '-63', '-2', '-54', '-26']
XX1 = ['63', '44', '85', '44', '81', '23', '90', '93', '23', '87', '47', '60', '94', '60', '102', '50', '93', '81', '17', '102', '106']
YY1 = ['5', '22', '4', '32', '22', '26', '14', '-6', '-27', '-25', '45', '-43', '-23', '48', '-1', '-48', '-33', '46', '40', '-29', '-24']
XX2 = ['60', '84', '101', '31', '94', '42', '55', '56', '89']
YY2 = ['61', '-55', '-42', '66', '-56', '72', '73', '-71', '-63']


def inputFarmList():
    # openUrl(urlFarmList)
    # time.sleep(1.5)
    i = 0
    while i < 22:
        click((337,366)) #isi kotak X
        erasee()
        write(XX2[i])
        click((391,364)) #isi kotak Y
        erasee()
        write(YY2[i])
        time.sleep(5)
        print(i)
        i = i + 1
    











def test1():
    # print(XX.index("93"))
    pass


def main():
    # singleLineParse()
    # coordIndex()
    # test1()
    inputFarmList()
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
