from BasicCommands import *
#region
#endregion
########## Variables  ###########
#region

########## Oasis Url  ###########
#region

urlTimeCountDown = 0

urlCity = "https://ttq.x2.asia.travian.com/dorf2.php"
urlSDA = "https://ttq.x2.asia.travian.com/dorf1.php"
urlFarmList = "https://ttq.x2.asia.travian.com/build.php?id=39&gid=16&tt=99"

def autoFarmList():
    click(chromeUrlBox)
    time.sleep(0.7)
    write(urlFarmList)
    enterr()
    time.sleep(2.3)
    click()

# (9, -8) Natar WW Village  
url0 = "https://ttq.x2.asia.travian.com/build.php?id=39&tt=2&z=327218&gid=16"
#url0Time = 3:26:31

"My URL"
urllMe = "https://ttq.x2.asia.travian.com/build.php?id=39&tt=2&z=323254&gid=16"

# (47,-1) IRON
url21 = "https://ttq.x2.asia.travian.com/build.php?id=39&tt=2&z=321649&gid=16"

#(52,-10) IRON
url22 = "https://ttq.x2.asia.travian.com/build.php?id=39&tt=2&z=328863&gid=16"

#endregion

########## Detecting Attack  ###########
#region
tempStartingPointForFindGGBCords = 536,230
tempStartingPointForFindGGBCords2 = 620,230
cordYangAdaWarna = 602,605,607
yellowRGB = 441
redRGB = 212
#endregion

########## Auto Farm Coordinates  ###########
#region
#Computer, 75% zoom, Split Screen sampai pas di gold coin besar
chromeUrlBox = 289, 62

mercenaryNumber = 307, 300
steepeRiderNumber = 415, 303

listTroopsType =[0,steepeRiderNumber, mercenaryNumber]

sendTroops = 298, 449
confirmSendTroops = 653, 435

########## Auto Detect Coordinates  ###########
mozilaBrowserCord = 217, 746
startAlarmVideo = 118, 182
WACord = 267,743
WAAccount = 167, 174
WACall = 1213,61

# chromeBrowserCord = 263, 744
# chromeBrowserSelectInstances = 263, 744

#endregion

########## Upgrade Building Coordinates  ###########
#region
clickUpgradeAds = 394, 419

warehouseCoord = 327, 269
granaryCoord = 286, 317
mainBuildingCoord = 375,318

upgradeWarehouse = 583, 527
upgradeGranary = 579, 527
upgradeMainBuilding = 578,468



cranny1=491, 233
cranny2=578, 252
cranny3=535, 287
cranny4=497, 330
cranny5=554, 424
cranny6=624, 455
cranny7=546, 482
cranny8=307, 433
cranny9=285, 386

upgradeCranny = 583, 586

listBuildingQueue = [
    cranny1,cranny2,cranny3,cranny4,cranny5,
    cranny6,cranny7,cranny8,cranny9
]
#endregion

########## Train Troops Coordinates  ###########
#region
stableCoord = 463, 482
scrollDownChrome = 802, 699
queueAllSteepeRider = 489, 555
queueAllSteepeRider2 = 488, 550
queueAllSteepeRider3 = 486, 606
queueAllSteepeRider4 = 487, 545 #pake mouse scroll
trainSteepeRider = 295, 693
trainSteepeRider2 = 298, 672
trainSteepeRider3 = 296, 664
trainSteepeRider4 = 300, 614 #pake mouse scroll
changeAttackMode = 459, 411
#endregion

#endregion

########## Farm Frequency Manager  ###########



farmScheduleCavalry =      min(listTimeFarm)

# Math --> jumlah tim minimum = 
# (hasil bagi masing-masing waktu terhadap waktu terpendek  
# --> hasil bagi wajib dibulatkan keatas
# Contoh --> waktu tempuh bolak balik masing masing --> 5, 10, 21 
# --> (5/5) + (10/5) + (21/5) = 1 + 2 + 5 = 8
def timeFarmCalculator():
    listTimeFarmDivided = []
    for i in listTimeFarm:
        listTimeFarmDividedResult = i/min(listTimeFarm)
        print(listTimeFarmDividedResult)
        # print(i)
        # print(len(listTimeFarm))
        listTimeFarmDivided.append(math.ceil(listTimeFarmDividedResult))
    # print(listTimeFarmDivided)
    print("Total Waves Needed: ",sum(listTimeFarmDivided))
    return listTimeFarmDivided

########## Temporary Coordinates  ###########

def upgradeBuilding(buildingCord,upgradeCord): #upgradeBuilding(warehouseCoord,upgradeWarehouse)
    click(chromeUrlBox)
    time.sleep(5)
    write(urlCity)
    enterr()
    time.sleep(5)
    click(buildingCord) 
    time.sleep(5)
    click(upgradeCord)
    time.sleep(5)
    click(clickUpgradeAds)
    print("ads clicked")
    time.sleep(90) #harus nungguin adsny putar selesai
    pass
def upgradeSDA(SDACord, upgradeSDACord):
    click(chromeUrlBox)
    time.sleep(5)
    write(urlSDA)
    enterr()
    time.sleep(5)
    click(SDACord) 
    time.sleep(5)
    click(upgradeSDACord)
    time.sleep(5)
    click(clickUpgradeAds)
    print("ads clicked")
    time.sleep(90) #harus nungguin adsny putar selesai
    pass

def trainTroops():
    click(chromeUrlBox)
    time.sleep(0.7)
    write(urlCity)
    enterr()
    time.sleep(2.3)
    click(stableCoord) 
    time.sleep(2)
    mouse.scroll(0,-2)
    time.sleep(0.5)

    rapidlyShiftingClick(487, 555, 666)
    time.sleep(0.5)
    rapidlyShiftingClick(297, 620, 700)
    
    print("Troops Trained")
    time.sleep(5)
       
def suicideNatar():
    raidUrl(url0,2,1)
    time.sleep(5)
    raidUrl(url0,2,1)
    time.sleep(5)
    raidUrl(url0,2,1)
    time.sleep(5)

def autoDetect():
    ### Detect Incoming Attacks
    click(chromeUrlBox)
    time.sleep(0.7)
    write(urlSDA)
    enterr()
    time.sleep(10.3) #biasa 2.3 dipasang 10.3 kalau lg lag
    currentIncomingStatus = GGBValueTestChosen((605,230))
    if currentIncomingStatus == 212:
        print("DANGER")
        click(mozilaBrowserCord)
        time.sleep(2)
        click(startAlarmVideo)
        time.sleep(5)
        click(WACord)
        time.sleep(1)
        click(WAAccount)
        time.sleep(1)
        click(WAAccount)
        time.sleep(1)
        click(WACall)
        time.sleep(0.5)
        click(WACall)
        time.sleep(0.5)
        click(WACall)
        time.sleep(0.5)

    else:
        print("chill")

def patrolAndBuild():
    while True:#patrol and build
        KK = 0
        LL = 9999
        while KK < LL: #cuman patroli incoming attacks
            if autoDetect() == "DANGER":
                print("Detected")
                break
            print("KK : ",KK)
            time.sleep(60)
            KK = KK + 1
        upgradeBuilding(mainBuildingCoord,upgradeMainBuilding)

        LL = LL * 1.25
        print(LL)

#Edit --> ganti index autoFarm(), ganti url & timeUrl
def patrolAndFarm():
    batchAmount = timeFarmCalculator()
    batchSent = [x*0 for x in batchAmount]
    while True:                 #patrol and farm
        autoFarm()
        print("sleeping for: ", farmScheduleCavalry," seconds")

        batchSent = [y+1  if y < x else x     for x, y in zip(batchAmount, batchSent) ]
        print("Batch Needed    : ", batchAmount)
        print("Batch Travelling: ", batchSent)
        # time.sleep(3)
        # trainTroops()
        autoDetect()

        i = 0
        while i < farmScheduleCavalry:
            print("Raid Time Cooldown: ",farmScheduleCavalry-i," secs left")
            i = i + 1
            time.sleep(1)
            if i % 60 == 0:
                autoDetect()
            pass

   
########## Detecting Attack  ###########

def GGBValueTestChosen(cord):
    # tempCoord = get_cords_only()
    RGBvalues = fullScreenGrab().getpixel(cord)
    print(RGBvalues)
    totall = sum(RGBvalues)
    print(totall)
    return totall

def GGBValueTest():
    tempCoord = get_cords_only()
    RGBvalues = fullScreenGrab().getpixel(tempCoord)
    print(RGBvalues)
    totall = sum(RGBvalues)
    print(totall)
    return totall, RGBvalues

def findGGBCords(x1,x2,y1):
    storeData =[]
    # x2 = x1 + 2
    while x1<x2:
        mouseCurrentLocation = x1,y1
        mousePos(mouseCurrentLocation)
        RGBTotal, RGBFound = GGBValueTest()
        newList = "RGBTotal is: "+ str(RGBTotal)+ " location: "+ str(mouseCurrentLocation)+ " RGBFound: "+ str(RGBFound)
        storeData.append(newList)
        x1 = x1+1
    print(storeData)

def scheduledAutoFarm():
    # time.sleep(600)
    # patrolAndBuild()
    # patrolAndFarm()

def test():
    list_1 = [1, 2, 3, 4, 5, 6]
    list_2 = [1, 2, 3, 0, 5, 6]

    # Print all items from list_1 that are not in list_2 ()
    a = [item for item in list_1 if item not in list_2]

    # Print all items from list_1 that differ from the item at the same index in list_2
    b = [x  if x != y else 100     for x, y in zip(list_1, list_2)    ]

    # Print all items from list_2 that differ from the item at the same index in list_1
    c = [y  if x != y else 100     for x, y in zip(list_1, list_2) ]
    print(a)
    print(b)
    print(c)
    
    # [1, 1, 1, 2, 1, 3]

def main():
    # test()
    # scheduledAutoFarm()
    # timeFarmCalculator()

    # autoDetect()
    # # click(queueAllSteepeRider4)
    # get_cords()
    # get_cords_only()
    # mousePos(tempStartingPointForFindGGBCords2)
    # findGGBCords(604,608,230)


    # testtt()
    # raidUrl1()
    # waitingTimeUpdate()
    # suicideNatar()
    # GGBValueTest()
    # listPrintCreator()
    
    # timeFarmSchedulingSystem()
    
    # autoFarm()
    # autoFarm(1)
    # trainTroops()

    
    pass

# spamFlyerPromo()


if __name__ == '__main__':
    main()


# %%(445, 437)(152, 538)
import os

# %%


