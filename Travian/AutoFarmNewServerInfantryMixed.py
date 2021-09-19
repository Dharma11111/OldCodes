from BasicCommands import *

########## Variables  ###########
#region
#endregion

########## Oasis Url  ###########

urlTimeCountDown = 0

urlCity = "https://ttq.x2.asia.travian.com/dorf2.php"
urlSDA = "https://ttq.x2.asia.travian.com/dorf1.php"

# (9, -8) Natar WW Village  
url0 = "https://ttq.x2.asia.travian.com/build.php?id=39&tt=2&z=327218&gid=16"
#url0Time = 3:26:31

"My URL"
urllMe = "https://ttq.x2.asia.travian.com/build.php?id=39&tt=2&z=323254&gid=16"


#"Yemn"
url1 = "https://ttq.x2.asia.travian.com/build.php?id=39&tt=2&z=328857&gid=16"

#"Blue" GAS 97pop
url2 = "https://ttq.x2.asia.travian.com/build.php?id=39&tt=2&z=328857&gid=16"

#"Tapchoi" 41,-6 92pop
url3 = "https://ttq.x2.asia.travian.com/build.php?id=39&tt=2&z=325648&gid=16"

#Percy GAS 72pop
url4 = "https://ttq.x2.asia.travian.com/build.php?id=39&tt=2&z=326444&gid=16"

# (52, -3) CLAY 10 menit 50 sda each
url5 = "https://ttq.x2.asia.travian.com/build.php?id=39&tt=2&z=323256&gid=16"
url5Time = (60 * 3 + 45)*2

# (53, -3) CLAY 15 menit ??? sda each
url6 = "https://ttq.x2.asia.travian.com/build.php?id=39&tt=2&z=323257&gid=16"
url6Time = (60 * 5 + 38)*2

# (47, -7) CLAY
url7 = "https://ttq.x2.asia.travian.com/build.php?id=39&tt=2&z=326455&gid=16"
url7Time = (60*9+23)*2

# (47, -8) CLAY
url8 = "https://ttq.x2.asia.travian.com/build.php?id=39&tt=2&z=327256&gid=16"
url8Time = (60*10+56)*2

# (42, -11) CLAY
url9 = "https://ttq.x2.asia.travian.com/build.php?id=39&tt=2&z=329654&gid=16"
url9Time = (60*21+13)*2

# (41, -11) CLAY
url10 = "https://ttq.x2.asia.travian.com/build.php?id=39&tt=2&z=329653&gid=16"
url10Time = (60*22+35)*2

listUrlFarm= [
    # url1,url2,url3,url4
    url5,url6,url7,url8,url9
]

#ngasal
# url1Time=2
# url2Time=2
# url3Time=2
# url4Time=2
# url5Time=2
# url6Time=2
# url7Time=2


########## Auto Farm Coordinates  ###########
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

# chromeBrowserCord = 263, 744
# chromeBrowserSelectInstances = 263, 744


########## Temporary Coordinates  ###########
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

########## Farm Frequency Manager  ###########

listTimeFarm = [
    # url1Time,
    # url2Time,
    # url3Time,
    # url4Time,
    url5Time,
    url6Time,
    url7Time,
    url8Time,
    url9Time,
]

# Math --> jumlah tim minimum = 
# (hasil bagi masing-masing waktu terhadap waktu terpendek  
# --> hasil bagi wajib dibulatkan keatas
# Contoh --> waktu tempuh bolak balik masing masing --> 5, 10, 21 
# --> (5/5) + (10/5) + (21/5) = 1 + 2 + 5 = 8
def timeFarmCalculator():
    for i in listTimeFarm:
        print(i/min(listTimeFarm))
        # print(i)
        # print(len(listTimeFarm))

farmScheduleCavalry =      min(listTimeFarm)
farmScheduleInfantry =      min(listTimeFarm)

listTimeFarmForSchedule =[
    farmScheduleCavalry,
    farmScheduleInfantry,
]

localFarmScheduleCavalry = farmScheduleCavalry
localFarmScheduleInfantry = farmScheduleInfantry
localListTimeFarmForSchedule = [localFarmScheduleCavalry,localFarmScheduleInfantry]


def timeFarmSchedulingSystem():
    global localFarmScheduleCavalry, localFarmScheduleInfantry, localListTimeFarmForSchedule
    
    earliestTime        = min(localListTimeFarmForSchedule)
    indexOfEarliestTime = localListTimeFarmForSchedule.index(earliestTime)
    print(earliestTime)
    print(indexOfEarliestTime)
    print(localListTimeFarmForSchedule)
    time.sleep(1)

    #kurangi waktu dgn waktu minimum
    i = 0
    while i < len(localListTimeFarmForSchedule):
        localListTimeFarmForSchedule[i] = localListTimeFarmForSchedule[i] - earliestTime
        print(localListTimeFarmForSchedule[i])
        i = i + 1

    print(localListTimeFarmForSchedule)

    #refill waktu yang habis
    localListTimeFarmForSchedule[indexOfEarliestTime] = listTimeFarmForSchedule[indexOfEarliestTime]
    print(localListTimeFarmForSchedule)
    print("cycle done")
    time.sleep(2)
    nextEarliestTime        = min(localListTimeFarmForSchedule)  #Tukar ini buat ganti frekuensi raid
    return indexOfEarliestTime, nextEarliestTime
    

########## Temporary Coordinates  ###########

def raidUrl(chosenUrl, typee=1, amount="2"):
    click(chromeUrlBox)
    time.sleep(0.7)
    write(chosenUrl)
    enterr()
    print("url written & entered")
    time.sleep(2)
    click(listTroopsType[typee])
    time.sleep(0.25)
    click(listTroopsType[typee]) #Solve Unclicked Textbox
    time.sleep(0.25)
    click(listTroopsType[typee]) #Solve Unclicked Textbox
    time.sleep(0.5)
    write(amount)
    time.sleep(0.5)
    click(changeAttackMode)
    time.sleep(0.5)
    click(sendTroops)
    time.sleep(1.5)
    click(confirmSendTroops)
    # print(chosenUrl, " is raided")

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

def tempFarm(startt, endd, typee, amount="2"):
    while startt <= endd:
        raidUrl(listUrlFarm[startt],typee,amount)
        time.sleep(3.5)
        print(startt,"th raid sent")
        startt = startt + 1
        
def suicideNatar():
    raidUrl(url0,2,1)
    time.sleep(5)
    raidUrl(url0,2,1)
    time.sleep(5)
    raidUrl(url0,2,1)
    time.sleep(5)

def autoFarm(raidBatch):

    if raidBatch == 0:
        #SteepeRider --> 5,6,12-15
        # tempFarm(5,5,1)
        # tempFarm(6,6,1)
        tempFarm(1,1,1,10)
        # tempFarm(12,13,1,1)
        # tempFarm(14,15,1,1)
        # tempFarm(16,20,1,1)
        # tempFarm(21,31,1,1)
        print("cavalry raided")

    if raidBatch == 1:
        #Mercenaries --> 1-4, 7-11 
        # tempFarm(1,1,2,20)      # 1 wave only
        # tempFarm(1,2,2)      # 2 wave only
        # tempFarm(1,4,2)
        # tempFarm(7,8,2)
        # tempFarm(8,12,2)
        print("infantry raided")
    
    # time.sleep(60*30+5)
    
    # while True:
    #     # time.sleep(60*30+5)
    #     tempFarm()
    #     tempFarm2()
    #     break

    # time.sleep(60*20+5)

def autoDetect():
    ### Detect Incoming Attacks
    click(chromeUrlBox)
    time.sleep(0.7)
    write(urlSDA)
    enterr()
    time.sleep(2.3)
    currentIncomingStatus = GGBValueTestChosen((605,230))
    if currentIncomingStatus == 212:
        condition = "DANGER"
        print(condition)

        return condition
    else:
        print("chill")


def scheduledAutoFarm():
    # timeFarmSchedulingSystem()
    # timeFarmSchedulingSystem()
    # time.sleep(600)
    # while True:#patrol and build
    #     KK = 0
    #     LL = 120
    #     while KK < LL: #cuman patroli incoming attacks
    #         if autoDetect() == "DANGER":
    #             print("Detected")
    #             break
    #         print("KK : ",KK)
    #         time.sleep(60)
    #         KK = KK + 1
    #     upgradeBuilding(mainBuildingCoord,upgradeMainBuilding)

    #     LL = LL * 1.25
    #     print(LL)
        

    while True:#patrol and farm

        currentIndex, raidTimeCooldown = timeFarmSchedulingSystem()
        autoFarm(currentIndex)
        print("sleeping for: ",raidTimeCooldown," seconds")

        trainTroops()
        if autoDetect() == "DANGER":
            print("Detected")
            break

        i = 0
        while i < raidTimeCooldown:
            print("Raid Time Cooldown: ",raidTimeCooldown-i," secs left")
            i = i + 1
            time.sleep(1)
            if i % 60 == 0:
                if autoDetect() == "DANGER":
                    print("Detected")
                    break
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

tempStartingPointForFindGGBCords = 536,230
tempStartingPointForFindGGBCords2 = 620,230
cordYangAdaWarna = 602,605,607
yellowRGB = 441
redRGB = 212

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



def main():
    scheduledAutoFarm()
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
    # timeFarmCalculator()
    
    # autoFarm(0)
    # autoFarm(1)
    # trainTroops()
    # while True:
        # timeFarmSchedulingSystem()
    pass

# spamFlyerPromo()


if __name__ == '__main__':
    main()


# %%(445, 437)(152, 538)
import os

# %%


