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
# from ZZZvariablesDataSDAupgrade import *

###################################################################
rawData = ""   ##Hasil Parse
index_pos_list = 0  ##Index Enter
###################################################################
#keywordSDAavailable = "Travian Plus allows you to make a link list."
keywordSDAproductionLumber = "Lumber:"
keywordSDAproductionClay = "Clay:"
keywordSDAproductionIron = "Iron:"
keywordSDAproductionCrop = "Crop:"
keywordUpgradeTimeLeft = "hrs. done at"
#keywordSDAtoUpgrade = "Description"

#keywordSDAPage="https://ts6.anglosphere.travian.com/dorf1.php"
#keywordCityPage="https://ts6.anglosphere.travian.com/dorf2.php"
keywordPage = ["",
               "https://ts6.anglosphere.travian.com/dorf1.php",
               "https://ts6.anglosphere.travian.com/dorf2.php"]
###################################################################
warehouse = 0
granary = 0

lumber = 0
clay = 0
iron = 0
crop = 0

lumberProd = 0
clayProd = 0
ironProd = 0
cropProd = 0


# For Upgrade
lumberNeeded = 0
clayNeeded   = 0
ironNeeded   = 0
cropNeeded   = 0


###################################################################

###################################################################


noww = datetime.datetime.now()
hourr = datetime.datetime.now().hour
minss = datetime.datetime.now().minute
secss = datetime.datetime.now().second + 3.5

dayss = datetime.datetime.now().day
monthh = datetime.datetime.now().month

currentTime = datetime.datetime.now()
upgradeDuration = 0
upgradeCompTime = 0  # Harus dipastiin cuman run sekali pas habis upgrade, prevent overwrite

hourLeft = 0
minsLeft = 0
secsLeft = 0
SDAPendingTime = 0

raidInterval = 0


###################### Main Functions  #######################
#input paste
def parse():
    global rawData
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
    rawData = resultt
##    print(resultt)
    return resultt

def printRaw():
    global rawData
    i = 0
    j = 0
    while j < len(rawData):
        print (rawData[i], " data ke", i)
        i = i + 1
        j = j + 1
    #print (rawData[4])
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def printRaw2():
    global rawData
    i = 0
    j = 0 
    k = [0]
    print( " ",end="")
    while j < 11: #create header horizontal
        print(j, "  ",end="")
        j = j + 1
    print( "", sep="" )
    while i < len(rawData):
        if i % 10 == 0:
            print("\n", k[0], end="")
            k[0] = k[0] + 1
        if rawData[i] == "\n":
            print("   ENTER",end="")
        print ("  ", rawData[i], end="")
        if rawData[i] == "\n":
            print("  ",end="")
        i = i + 1
    #print (rawData[4])
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def timee(hrs,mins,secs,days):
    return datetime.timedelta(hours=hrs, minutes=mins, seconds=int(secs), days=int(days))

def indexSpace():
    global rawData, index_pos_list
    index_pos_list = list(locate(rawData, lambda a: a == '\n')) ##    print('Indexes of all occurrences of a "Ok" in the list are : ', index_pos_list)
    return index_pos_list

def cleanInt(variable):
    clean = ''.join(c for c in variable if c.isdigit()) ##    print(clean)
    return int(clean)

def findDataIndex(keyword):
    global rawData
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print (rawData.find(keyword))
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return rawData.find(keyword)

def findEnter(keyword,*m):
    global indexx
    global index_pos_list
    indexSpace()
    indexx = findDataIndex(keyword)
    for n in index_pos_list:
        if n > indexx:
            indexNumber = index_pos_list.index(n)
            for X in m:
                indexNumber = indexNumber + X
            return index_pos_list[indexNumber]

def collectSingleDataProd(keyword):
    global rawData
    Point1 = findDataIndex(keyword)
    Point2 = findEnter(keyword)
##    print("Point1: ", Point1, "Point2", Point2, "data beg to end: ", rawData[Point1:Point2])

    if keyword == keywordSDAproductionLumber:
        # print("-",rawData[ Point1+9 :Point2-1 ],"-")
        return cleanInt(rawData[ Point1+9 :Point2-1 ])   #toggle str & int
    else:
        return cleanInt(rawData[ Point1+7 :Point2-1 ])

def collectAllDataProd():
    global lumberProd, clayProd, ironProd, cropProd
    lumberProd = collectSingleDataProd(keywordSDAproductionLumber)
    clayProd = collectSingleDataProd(keywordSDAproductionClay)
    ironProd = collectSingleDataProd(keywordSDAproductionIron)
    cropProd = collectSingleDataProd(keywordSDAproductionCrop)
##    print(lumberProd, clayProd, ironProd, cropProd)
    print("\n",
          "lumberProd: ",lumberProd, "\n",
          "clayProd:   ",clayProd, "\n",
          "ironProd:   ",ironProd, "\n",
          "cropProd:   ",cropProd, "\n")
    
def collectDataCapacity():
    global rawData
    global warehouse, granary, lumber, clay, iron, crop
    keyword = "Travian Plus allows you to make a link list."
    
    Point0 = findEnter(keyword,0)
    Point1 = findEnter(keyword,1)
    Point2 = findEnter(keyword,2)
    Point3 = findEnter(keyword,3)
    Point4 = findEnter(keyword,4)
    Point5 = findEnter(keyword,5)
    Point6 = findEnter(keyword,6)
##    print("***", Point0, Point1, Point2), Point3, Point4, Point5, Point6)
##    print("LOL", rawData[Point4:Point5])
##    print("LOL", rawData[Point5:Point6])
    
    warehouse = str(rawData[ Point0 + 1 :Point1 - 2 ])
    lumber = str(rawData[ Point1 + 1 :Point2 ]) 
    clay = str(rawData[ Point2 + 1 :Point3 ])
    iron = str(rawData[ Point3 + 1 :Point4 ])
    granary = str(rawData[ Point4 + 2 :Point5 - 2 ])
    crop = str(rawData[ Point5 + 1 :Point6 ])
##    print(warehouse,lumber,clay,iron,granary,crop)
    warehouse = cleanInt(warehouse)*10
    granary = cleanInt(granary)*10
    lumber = cleanInt(lumber)
    clay = cleanInt(clay)
    iron = cleanInt(iron)
    crop = cleanInt(crop)
    print("Available \n",
          "warehouse: ",warehouse, "\n",
          "lumber:    ",lumber, "\n",
          "clay:      ",clay, "\n",
          "iron:      ",iron, "\n",
          "granary:   ",granary, "\n",
          "crop:      ",crop, "\n")
##def collectDataDorf():
##    parse()
##    collectAllDataProd()
##    collectDataCapacity()
##    pass

def forecastSDA():
##    global warehouse, granary, lumber, clay, iron, crop
    TList = [warehouse, granary, lumber, clay, iron, crop]
    selectedSDA = 0
    TList[2] = (TList[0]-TList[2]) / lumberProd
    TList[3] = (TList[0]-TList[3]) / clayProd
    TList[4] = (TList[0]-TList[4]) / ironProd
    TList[5] = (TList[1]-TList[5]) / cropProd
    indexSmallest = TList.index(min(TList))

    secsToFull = TList[indexSmallest]*3600
##    print(secsToFull)
    fullIn = timee(0,0,secsToFull)

    TList[2] = lumber + secsToFull / 3600 * lumberProd
    TList[3] = clay + secsToFull / 3600 * clayProd
    TList[4] = iron + secsToFull / 3600 * ironProd
    TList[5] = crop + secsToFull / 3600 * cropProd

    print("Hasil forecast Full in:  ",fullIn,"\n",
          "lumber: ",int(TList[2]),  "\n",
          "clay:   ",int(TList[3]),  "\n",
          "iron:   ",int(TList[4]),  "\n",
          "crop:   ",int(TList[5]))
    pass
    

def upgradeTimeLeft():
    global upgradeDuration, upgradeCompTime, hourLeft, minsLeft, secsLeft
    Point1 = findDataIndex(keywordUpgradeTimeLeft)    # Titik awal
    Point2 = findEnter(keywordUpgradeTimeLeft)        # Titik akhir

##    print("Point1: ", Point1, "Point2", Point2,
##          "data beg to end: ", rawData[Point1:Point2])
    timeComp = rawData[Point1:Point2]
    # Index Finding
    timeCompSep = timeComp.find(":")                  # Titik tengah ":"
    # Actual Value
    compHour = int(timeComp[timeCompSep - 2])*10 + int(timeComp[timeCompSep - 1])
    compMins = int(timeComp[timeCompSep + 1])*10 + int(timeComp[timeCompSep + 2])
    
    print("Complete Hour: ",compHour, "Complete Mins: ",compMins)
    
    Point3 = Point1 - 9                               # Titik awal

    hourLeft = int(rawData[Point3    ])*10 + int(rawData[Point3 + 1])
    minsLeft = int(rawData[Point3 + 3])*10 + int(rawData[Point3 + 4])
    secsLeft = int(rawData[Point3 + 6])*10 + int(rawData[Point3 + 7])

    nowwTotal = hourr    * 60 + minss         # in minutes
    compTotal = compHour * 60 + compMins + 5  # in minutes   with buffer 5 minutes
    leftTotal = hourLeft * 60 + minsLeft      # in minutes

    if compTotal < nowwTotal:                 # solve kalau selesai nya besok
        compTotal = compTotal + (24 * 60)     # in minutes
    if nowwTotal + leftTotal > compTotal:
        hourLeft = int(rawData[Point3 + 1])

##    timeLeft = rawData[Point1 - 9 :Point1]
##    print("time Left: ",timeLeft,
##          "Total Now: ",nowwTotal,
##          "Total comp: ",compTotal,
##          "Total Left: ",leftTotal)
    print("hour left: ",hourLeft,
          "\n minutes left: ", minsLeft,
          "\n secs left: ", secsLeft)
    upgradeDuration = timee(hourLeft,minsLeft,secsLeft,0)
    upgradeCompTime = currentTime + upgradeDuration
    print(" Upgrade Duration:        ", upgradeDuration,
          "\n Upgrade Complete Time: ", upgradeCompTime)
    return timee(hourLeft,minsLeft,secsLeft,0)
##def upgradeTimeLeft2():
##    parse()
##    upgradeTimeLeft()
##    pass

def SDAtoUpgrade():
    global lumberNeeded, clayNeeded, ironNeeded, cropNeeded
    keyword = "Description"
    i = 0
    
    while not rawData[ findEnter(keyword,i) +1].isdigit():
        i = i + 1
        Point1 = findEnter(keyword,i)

    Point2 = findEnter(keyword,i+1)
    Point3 = findEnter(keyword,i+2)
    Point4 = findEnter(keyword,i+3)
    Point5 = findEnter(keyword,i+4)
    
    lumberNeeded = str(rawData[ Point1 + 1 :Point2 ])
    clayNeeded   = str(rawData[ Point2 + 1 :Point3 ])
    ironNeeded   = str(rawData[ Point3 + 1 :Point4 ])
    cropNeeded   = str(rawData[ Point4 + 1 :Point5 ])

    lumberNeeded = cleanInt(lumberNeeded)
    clayNeeded   = cleanInt(clayNeeded)
    ironNeeded   = cleanInt(ironNeeded)
    cropNeeded   = cleanInt(cropNeeded)
    print("SDA Needed to Upgrade \n",
          "lumber Needed:    ",lumberNeeded, "\n",
          "clay   Needed:    ",clayNeeded, "\n",
          "iron   Needed:    ",ironNeeded, "\n",
          "crop   Needed:    ",cropNeeded, "\n")
##def SDAandTimetoUpgrade2():
##    parse()
##    SDAtoUpgrade()
##    calcSDAPendingTime()
##    pass


def calcSDAPendingTime():
    global SDAPendingTime

##    upgradeDurationInHour      = hourLeft + minsLeft*60 + secsLeft*3600
##    lumberWhenUpgradeComplete  = lumber + lumberProd * upgradeDurationInHour
##    clayWhenUpgradeComplete    = clay   + clayProd   * upgradeDurationInHour
##    ironWhenUpgradeComplete    = iron   + ironProd   * upgradeDurationInHour
##    cropWhenUpgradeComplete    = crop   + cropProd   * upgradeDurationInHour
##    lumberTime  =( lumberNeeded - lumberWhenUpgradeComplete ) / lumberProd
##    clayTime    =( clayNeeded   - clayWhenUpgradeComplete   ) / clayProd
##    ironTime    =( ironNeeded   - ironWhenUpgradeComplete   ) / ironProd
##    cropTime    =( cropNeeded   - cropWhenUpgradeComplete   ) / cropProd
    lumberTime  =( lumberNeeded - lumber ) / lumberProd
    clayTime    =( clayNeeded   - clay   ) / clayProd
    ironTime    =( ironNeeded   - iron   ) / ironProd
    cropTime    =( cropNeeded   - crop   ) / cropProd
    print("1",ironTime)
    longestTime = max(lumberTime, clayTime, ironTime, cropTime)  # in hour
    print("2",longestTime)
    SDAPendingTime = longestTime if longestTime > 0 else 0
    print("3",SDAPendingTime)
    return SDAPendingTime

def collectDataAll():     #***********   Head Code  *******#
    
    
    try:#***** Parse data *****#
        parse()
    except Exception:
        pass
####    printRaw()
    try:#***** Collect production data *****#
        collectAllDataProd()
    except Exception:
        pass
    try:#***** SDA Available *****#
        collectDataCapacity()
    except Exception:
        pass
    try:#***** Forecast SDA *****#
        forecastSDA()
    except Exception:
        pass
    try:#***** Upgrade Time  *****#
        upgradeTimeLeft()
    except Exception:
        pass
    try:#***** SDA Needed To Upgrade  *****#
        SDAtoUpgrade()
    except Exception:
        pass
    try:#***** SDA Needed To Upgrade  *****#
        calcSDAPendingTime()
    except Exception:
        pass

################# Main Logic                        ################

def doneLoad():
    while True:
        if confirmRGBValue((246,275)) == 668:
            time.sleep(1)
            break
    pass

def openDorfParameter(dorf,parameter):
    click(UrlBoxChrome)
    keyboard.type(keywordPage[dorf])
    enterr()
    doneLoad()
    click(parameter)
    doneLoad()
    time.sleep(1)
    
def checkSDAAvailability(dorf,parameter):
    # update speed production & jumlah SDA
    click(UrlBoxChrome)
    keyboard.type(keywordPage[1])
    enterr()
    doneLoad()

    pullNewData()
    parse()
    collectAllDataProd()
    collectDataCapacity()
    
    # cek SDA availability
    openDorfParameter(dorf,parameter)
    
    pullNewData()
    parse()
    SDAtoUpgrade()
    calcSDAPendingTime()
    print("4",SDAPendingTime)
    print("Need to wait SDA for ",SDAPendingTime*3600," seconds")
    pass

def build(dorf, parameter):
    ### clicks buat upgrade  ###
    openDorfParameter(dorf,parameter)
    click(SDAUpgradeButton)
    ### collect data durasi upgrade  ###
    pullNewData()
    parse()
    upgradeTimeLeft()

    pass

def setUpAndPositionShell(): # Pertama kali buka nge bug posisi awal nya
    temp0 = [453 , 60]
    temp1 = [924 , 12]
    temp2 = [1365, 222]
    temp3 = [1012, 12]
    temp4 = [681 , 246]
    temp5 = [1093, 308]
    temp6 = [684 , 538]
    time.sleep(1)
    click(temp1)
    time.sleep(1)
##    drag(temp1,temp2)
##    time.sleep(0.5)
##    click(temp3)
##    time.sleep(0.5)
    drag(temp6,temp5)
    time.sleep(0.5)
    click(FirstTabChrome)

def pullNewData(): #isi sesama python
    temp1 = [224 , 750]
    temp2 = [206 , 664]
    click(temp1)
    time.sleep(0.5)
    click(temp2)
    keyboard.press(Key.f5)
    keyboard.release(Key.f5)




    
################# TestingFunctions                  ################

def decideNext():
    global SDAPendingTime, upgradeDuration, raidInterval, hourLeft, minsLeft, secsLeft


def a2():
    global AA,BB,CC
    print(timee(5,5,5,0)-timee(7.5,0,0,0))
##    print(timee(hourr,minss,secss,dayss))
##    print(noww - timee(3,3,3,0))
    pass

bob = 0
def a3():
    global bob
    bob = 5
    print(bob)
    pass

def main():
    global rawData
    parse()
    printRaw2()
    # collectDataAll()
    # collectAllDataProd()
    # findDataIndex("Legionnaires")
    print(rawData[890:895])


##    print(datetime.datetime.now(), noww, hourr, minss, secss)

    pass
    
 
if __name__ == '__main__':
    main()



#end


#        NOTES         #
#print(datetime.datetime.now())       ini telat 3,5 detik dibanding travian
# %%

# %%
def a4():
    global bob
    bob = 5
    print(bob)
    pass
# %%