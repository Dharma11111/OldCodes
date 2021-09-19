from BasicCommands import *
#region
#endregion
########## Variables  ###########
#region

########## Oasis Url  ###########
#region

urlTimeCountDown = 0

urlCity = "https://ts3.x1.asia.travian.com/dorf2.php"
urlSDA = "https://ts3.x1.asia.travian.com/dorf1.php"
urlFarmList = "https://ts3.x1.asia.travian.com/build.php?id=39&gid=16&tt=99"
urlVillage1 = 760, 360
urlVillage2 = 762, 374


farmListStart1 = 620,337
farmListStart2 = 620,377
farmListStart3 = 620,407
farmListStart4 = 620,443
urlEnemy = "https://ts3.x1.asia.travian.com/profile/10292"

def autoFarmList():
    click(urlVillage1)
    time.sleep(2)
    click(chromeUrlBox)
    time.sleep(0.7)
    write(urlFarmList)
    enterr()
    time.sleep(2.3)
    # click(farmListStart4)
    # time.sleep(1)
    # click(farmListStart3)
    # time.sleep(1)
    click(farmListStart2)
    time.sleep(1)
    click(farmListStart1)
    time.sleep(1)

def autoUrlFarm(chosenUrl, typee=2, amount="999"):
    click(urlvillage1)
    time.sleep(2)
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
    click(listTroopsType[0]) #Solve Unclicked Textbox
    time.sleep(0.5)
    write("1")
    time.sleep(0.5)
    click(changeAttackMode)
    time.sleep(0.5)
    click(sendTroops)
    time.sleep(1.5)
    click(confirmSendTroops)
    time.sleep(3)
    # print(chosenUrl, " is raided")

# (9, -8) Natar WW Village  
url0 = "https://ttq.x2.asia.travian.com/build.php?id=39&tt=2&z=327218&gid=16"
#url0Time = 3:26:31

"My URL"
urllMe = "https://ts3.x1.asia.travian.com/build.php?id=39&tt=2&z=323254&gid=16"

url1 = "https://ts3.x1.asia.travian.com/build.php?id=39&tt=2&z=119556&gid=16"

url2 = "https://ts3.x1.asia.travian.com/build.php?id=39&tt=2&z=119160&gid=16"

url3 = "https://ts3.x1.asia.travian.com/build.php?id=39&tt=2&z=120761&gid=16"

url4 = "https://ts3.x1.asia.travian.com/build.php?id=39&tt=2&z=121571&gid=16"
url5 = "https://ts3.x1.asia.travian.com/build.php?id=39&tt=2&z=121171&gid=16"
url6 = "https://ts3.x1.asia.travian.com/build.php?id=39&tt=2&z=120369&gid=16"
url7 = "https://ts3.x1.asia.travian.com/build.php?id=39&tt=2&z=118360&gid=16"
url8 = "https://ts3.x1.asia.travian.com/build.php?id=39&tt=2&z=117182&gid=16"
url9 = "https://ts3.x1.asia.travian.com/build.php?id=39&tt=2&z=117583&gid=16"
url10 = "https://ts3.x1.asia.travian.com/build.php?id=39&tt=2&z=117984&gid=16"

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

heroIcon = 192, 112
adventureTab = 530, 249
adventureButton = 623, 410

heroNumber = 633,349
steepeRiderNumber = 415, 303
mercenaryNumber = 307, 300

listTroopsType =[heroNumber,steepeRiderNumber, mercenaryNumber,]

changeAttackMode = 459, 411
sendTroops = 298, 449
confirmSendTroops = 653, 435

########## Auto Detect Coordinates  ###########
mozilaBrowserCord = 217, 746
startAlarmVideo = 118, 182
WACord = 267,743
WAAccount = 167, 174
WACall = 1213,61
WAChatBox = 614,703

# chromeBrowserCord = 263, 744
# chromeBrowserSelectInstances = 263, 744

#endregion

########## Upgrade Building Coordinates  ###########
#region
clickUpgradeAds = 394, 419

warehouseCoord = 327, 269
granaryCoord = 286, 317
mainBuildingCoord = 375,318
rallyPointCoord = 608,350
townHallCoord = 623, 465
heroMansionCoord = 273,401

upgradeTownHall = 577, 562
upgradeRallyPoint = 586,515
upgradeWarehouse = 583, 468
upgradeGranary = 579, 472
upgradeMainBuilding = 578,468
upgradeHeroMansion = 479,604



sda1 = 331, 265
sda2 = 401, 266
sda3 = 468, 266
sda4 = 304, 291
sda5 = 402, 309
sda6 = 427, 306
sda7 = 505, 304
sda8 = 261, 329
sda9 = 313, 331
sda10 = 471, 326
sda11 = 532, 324
sda12 = 261, 373
sda13 = 315, 370
sda14 = 507, 374
sda15 = 405, 389
sda16 = 329, 428
sda17 = 404, 426
sda18 = 478, 418
upgradeSDACoord = 581, 467

coordSDAList = [sda1, sda2, sda3, sda4, sda5, sda6, sda7, sda8, sda9, sda10, sda11, sda12, sda13, sda14, sda15, sda16, sda17, sda18]
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

#endregion

#endregion

########## Farm Frequency Manager  ###########

listTimeFarm = []

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

def currentTime():
    return str(time.asctime( time.localtime(time.time()) ))
def targetTime(ExtraTime):
    return str(time.asctime( time.localtime(   time.time() + ExtraTime ) ))

def openUrl(desiredUrl):
    click(chromeUrlBox)
    time.sleep(5)
    write(desiredUrl)
    enterr()
    time.sleep(5)
    pass

def upgradeBuilding(buildingCord,upgradeCord): #upgradeBuilding(warehouseCoord,upgradeWarehouse)
    openUrl(urlCity)
    click(buildingCord) 
    time.sleep(5)
    click(upgradeCord)
    time.sleep(5)
    # click(clickUpgradeAds)
    # print("ads clicked")
    # time.sleep(90) #harus nungguin adsny putar selesai
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

    rapidlyShiftingClick(487, 444, 666)
    time.sleep(0.5)
    rapidlyShiftingClick(297, 570, 700)
    
    print("Troops Trained")
    time.sleep(5)

def startAdventure():
    time.sleep(2)
    openUrl(urlSDA)
    time.sleep(2)
    click(heroIcon)
    time.sleep(2)
    click(adventureTab)
    time.sleep(2)
    click(adventureButton)
    time.sleep(2)
    openUrl(urlSDA)
    time.sleep(2)
    pass

def autoDetect():
    ### Detect Incoming Attacks
    click(chromeUrlBox)
    time.sleep(0.7)
    write(urlSDA)
    enterr()
    time.sleep(2.3) #biasa 2.3 dipasang 10.3 kalau lg lag
    # mousePos((605,230))
    currentIncomingStatus = GGBValueTestChosen((606,230))
    if currentIncomingStatus == 212:
        print("DANGER")
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
        click(mozilaBrowserCord)
        time.sleep(2)
        click(startAlarmVideo)
        time.sleep(5)

    else:
        print("chill")

def patrolAndBuild():
    while True:#patrol and build
        KK = 0
        LL = 60
        while KK < LL: #cuman patroli incoming attacks
            if KK % 3 == 0:
                collectPop() # temporary
            if KK % 2 == 0:
                autoFarmList()
            if autoDetect() == "DANGER":
                print("Detected")
                break
            print("KK : ",KK)
            
            time.sleep(60*4)
            KK = KK + 1
        upgradeBuilding(granaryCoord,upgradeGranary)

        LL = LL * 1.25
        print(LL)

farmListSchedule = 1*(5*2*30)*8/10
def patrolAndFarm():
    time.sleep(1)
    
    batchAmount = timeFarmCalculator()
    batchSent = [x*0 for x in batchAmount]
    # upgrade building
    upgradeBuildingTimer = 1
    customActionIncrement = 1
    currentTimeForUpgradeInt = time.time()
    targetTime1 = targetTime(60*315)#((45*26))
    targetTime2 = targetTime(60*315+60*400)#targetTime1 + targetTime(3*45)#(45*26)
    targetTime3 = targetTime(60*315+60*400+60*460)#####targetTime2 + targetTime(45*10)
    targetTime4 = targetTime(60*85+60*290+60*340+60*400)
    targetTime5 = targetTime(60*85+60*290+60*340+60*400+60*460)
    targetTime6 = targetTime(70*60+60*160+60*185+60*215+60*250+60*290)
    targetTime7 = targetTime(70*60+60*160+60*185+60*215+60*250+60*290+60*340)
    targetTime8 = targetTime(70*60+60*160+60*185+60*215+60*250+60*290+60*340+60*395)
    targetTime9 = targetTime(70*60+60*160+60*185+60*215+60*250+60*290+60*340+60*395+60*440)
    targetTime10 = targetTime((0))
    targetTime11 = targetTime((0))
    targetTime12 = targetTime((0))
    targetTime13 = targetTime((0))

    # upgrade building
    while True:                 #patrol and farm
        # autoFarmList()
        # autoUrlFarm(url1)

        print("sleeping for: ", farmListSchedule," seconds")
        batchSent = [y+1  if y < x else x     for x, y in zip(batchAmount, batchSent) ]
        print("Batch Needed    : ", batchAmount)
        print("Batch Travelling: ", batchSent)
        # time.sleep(3)
        # trainTroops()
        autoDetect()
        collectPop() # temporary

        print("custom action increment is currently: ",customActionIncrement)
        # if customActionIncrement % (40) == 0:
        #     trainTroops()
        # if customActionIncrement % (14*2) == 0:
        #     startAdventure()
        customActionIncrement = customActionIncrement + 1
        i = 0
        while i < farmListSchedule + random.randint(1,15):
            print("Raid Time Cooldown: ",farmListSchedule-i," secs left, i is: ",i%60)
            i = i + 1
            time.sleep(1)
            if i % 60 == 0:
                autoDetect()
            pass
        
        continue

        #upgrade building section
        print("currentTimeForUpgradeUpdate: ", str(time.asctime( time.localtime(time.time()-currentTimeForUpgradeInt) )), " elapsed")
        if upgradeBuildingTimer == 1 and currentTime()>targetTime1:
            upgradeBuilding(heroMansionCoord,upgradeHeroMansion) 
            print("upgradeBuildingTimer: ", upgradeBuildingTimer," selesai")
            upgradeBuildingTimer = upgradeBuildingTimer + 1
        # continue
        if upgradeBuildingTimer == 2 and currentTime()>targetTime2:
            upgradeBuilding(heroMansionCoord,upgradeHeroMansion) #ini up ke lvl 16, harus nunggu selama (waktu up lvl 15) plus 5 menit buffer
            print("upgradeBuildingTimer: ", upgradeBuildingTimer," selesai")
            upgradeBuildingTimer = upgradeBuildingTimer + 1
        
        if upgradeBuildingTimer == 3 and currentTime()>targetTime3:
            upgradeBuilding(heroMansionCoord,upgradeHeroMansion) #ini up ke lvl 17
            print("upgradeBuildingTimer: ", upgradeBuildingTimer," selesai")
            upgradeBuildingTimer = upgradeBuildingTimer + 1
        # continue
        if upgradeBuildingTimer == 4 and currentTime()>targetTime4:
            upgradeBuilding(heroMansionCoord,upgradeHeroMansion)
            print("upgradeBuildingTimer: ", upgradeBuildingTimer," selesai")
            upgradeBuildingTimer = upgradeBuildingTimer + 1

        if upgradeBuildingTimer == 5 and currentTime()>targetTime5: #4jam lbh estimated
            upgradeBuilding(heroMansionCoord,upgradeHeroMansion) #ini up ke lvl 15
            print("upgradeBuildingTimer: ", upgradeBuildingTimer," selesai")
            upgradeBuildingTimer = upgradeBuildingTimer + 1
        
        if upgradeBuildingTimer == 6 and currentTime()>targetTime6: # +52+62+39+46+54: 
            upgradeBuilding(heroMansionCoord,upgradeHeroMansion) #ini up ke lvl 16
            print("upgradeBuildingTimer: ", upgradeBuildingTimer," selesai")
            upgradeBuildingTimer = upgradeBuildingTimer + 1

        if upgradeBuildingTimer == 7 and currentTime()>targetTime7: # 
            upgradeBuilding(heroMansionCoord,upgradeHeroMansion) #ini up wood ke lvl 7
            print("upgradeBuildingTimer: ", upgradeBuildingTimer," selesai")
            upgradeBuildingTimer = upgradeBuildingTimer + 1
        
        if upgradeBuildingTimer == 8 and currentTime()>targetTime8: # 
            upgradeBuilding(heroMansionCoord,upgradeHeroMansion) #ini up wood ke lvl 7
            print("upgradeBuildingTimer: ", upgradeBuildingTimer," selesai")
            upgradeBuildingTimer = upgradeBuildingTimer + 1
        
        if upgradeBuildingTimer == 9 and currentTime()>targetTime9: # 
            upgradeBuilding(heroMansionCoord,upgradeHeroMansion) #ini up wood ke lvl 7
            print("upgradeBuildingTimer: ", upgradeBuildingTimer," selesai")
            upgradeBuildingTimer = upgradeBuildingTimer + 1

        continue
        
        if upgradeBuildingTimer == 10 and currentTime()>targetTime10: # 
            upgradeBuilding(townHallCoord,upgradeTownHall) #ini up wood ke lvl 7
            print("upgradeBuildingTimer: ", upgradeBuildingTimer," selesai")
            upgradeBuildingTimer = upgradeBuildingTimer + 1
        
        if upgradeBuildingTimer == 11 and currentTime()>targetTime11: # 
            upgradeSDA(sda15,upgradeSDACoord) #ini up wood ke lvl 7
            print("upgradeBuildingTimer: ", upgradeBuildingTimer," selesai")
            upgradeBuildingTimer = upgradeBuildingTimer + 1
        
        if upgradeBuildingTimer == 12 and currentTime()>targetTime12: # 
            upgradeSDA(sda17,upgradeSDACoord) #ini up wood ke lvl 7
            print("upgradeBuildingTimer: ", upgradeBuildingTimer," selesai")
            upgradeBuildingTimer = upgradeBuildingTimer + 1
        
        if upgradeBuildingTimer == 13 and currentTime()>targetTime13: # 
            upgradeSDA(sda1,upgradeSDACoord) #ini up wood ke lvl 7
            print("upgradeBuildingTimer: ", upgradeBuildingTimer," selesai")
            upgradeBuildingTimer = upgradeBuildingTimer + 1

        # continue
        print("currentTimeForUpgradeUpdate: ", str(time.asctime( time.localtime(time.time()-currentTimeForUpgradeInt) )), " elapsed")
        if upgradeBuildingTimer == 1 and currentTime()>targetTime1:
            time.sleep(2)
            click(urlVillage2)
            time.sleep(2)
            autoUrlFarm(url1,0,1)
            time.sleep(2)
            click(urlVillage1)
            time.sleep(2)
            print("upgradeBuildingTimer: ", upgradeBuildingTimer," selesai")
            upgradeBuildingTimer = upgradeBuildingTimer + 1
        if upgradeBuildingTimer == 2 and currentTime()>targetTime2:
            time.sleep(2)
            click(urlVillage2)
            time.sleep(2)
            autoUrlFarm(url2,0,1)
            time.sleep(2)
            click(urlVillage1)
            time.sleep(2)
            print("upgradeBuildingTimer: ", upgradeBuildingTimer," selesai")
            upgradeBuildingTimer = upgradeBuildingTimer + 1
        # continue
        if upgradeBuildingTimer == 3 and currentTime()>targetTime3:
            time.sleep(2)
            click(urlVillage2)
            time.sleep(2)
            autoUrlFarm(url3,0,1)
            time.sleep(2)
            click(urlVillage1)
            time.sleep(2)
            print("upgradeBuildingTimer: ", upgradeBuildingTimer," selesai")
            upgradeBuildingTimer = upgradeBuildingTimer + 1
        if upgradeBuildingTimer == 4 and currentTime()>targetTime4:
            time.sleep(2)
            click(urlVillage2)
            time.sleep(2)
            autoUrlFarm(url4,0,1)
            time.sleep(2)
            click(urlVillage1)
            time.sleep(2)
            print("upgradeBuildingTimer: ", upgradeBuildingTimer," selesai")
            upgradeBuildingTimer = upgradeBuildingTimer + 1
        if upgradeBuildingTimer == 5 and currentTime()>targetTime5:
            time.sleep(2)
            click(urlVillage2)
            time.sleep(2)
            autoUrlFarm(url5,0,1)
            time.sleep(2)
            click(urlVillage1)
            time.sleep(2)
            print("upgradeBuildingTimer: ", upgradeBuildingTimer," selesai")
            upgradeBuildingTimer = upgradeBuildingTimer + 1
        if upgradeBuildingTimer == 6 and currentTime()>targetTime6:
            time.sleep(2)
            click(urlVillage2)
            time.sleep(2)
            autoUrlFarm(url6,0,1)
            time.sleep(2)
            click(urlVillage1)
            time.sleep(2)
            print("upgradeBuildingTimer: ", upgradeBuildingTimer," selesai")
            upgradeBuildingTimer = upgradeBuildingTimer + 1
        if upgradeBuildingTimer == 7 and currentTime()>targetTime7:
            time.sleep(2)
            click(urlVillage2)
            time.sleep(2)
            autoUrlFarm(url7,0,1)
            time.sleep(2)
            click(urlVillage1)
            time.sleep(2)
            print("upgradeBuildingTimer: ", upgradeBuildingTimer," selesai")
            upgradeBuildingTimer = upgradeBuildingTimer + 1
        
        if upgradeBuildingTimer == 8 and currentTime()>targetTime8:
            time.sleep(2)
            click(urlVillage2)
            time.sleep(2)
            autoUrlFarm(url8,0,1)
            time.sleep(2)
            click(urlVillage1)
            time.sleep(2)
            print("upgradeBuildingTimer: ", upgradeBuildingTimer," selesai")
            upgradeBuildingTimer = upgradeBuildingTimer + 1
        continue
        if upgradeBuildingTimer == 9 and currentTime()>targetTime9:
            time.sleep(2)
            click(urlVillage2)
            time.sleep(2)
            autoUrlFarm(url9,0,1)
            time.sleep(2)
            click(urlVillage1)
            time.sleep(2)
            print("upgradeBuildingTimer: ", upgradeBuildingTimer," selesai")
            upgradeBuildingTimer = upgradeBuildingTimer + 1
        continue 
    
        
        


   
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
    patrolAndFarm()

def waveBuilder():
    i=0
    while i<5:
        click((617,23))
        keyboard.press(Key.ctrl)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.release(Key.ctrl)
        click((650,443))
        i=i+1
    pass

def collectPop():
    openUrl(urlEnemy)
    # click((650,577))
    time.sleep(1)
    # mouse.scroll(0,-3)
    # time.sleep(0.5)
    # drag((674,538),(677,616))#fem
    drag((640,526),(665,639))#lonelywolfy
    time.sleep(1)
    copyy()
    time.sleep(1)
    click(WACord)
    time.sleep(1)
    click(WAAccount)
    time.sleep(1)
    click(WAAccount)
    time.sleep(1)
    click(WAChatBox)
    time.sleep(1)
    click(WAChatBox)
    time.sleep(1)
    pastee()
    time.sleep(1)
    enterr()
    time.sleep(1)
    click(WACord)
    time.sleep(1)
    pass


def tempChiefNatar():
    openUrl("https://ttq.x2.asia.travian.com/build.php?id=39&tt=2&z=328854&gid=16")
    click((414,301))
    time.sleep(2)
    write("150")
    click((416,348))
    time.sleep(2)
    write("15")
    click((632,303))
    time.sleep(2)
    write("1")
    time.sleep(2)
    click((631,351))
    time.sleep(2)
    write("1")
    time.sleep(2)
    click(sendTroops)
    time.sleep(5)
    click(confirmSendTroops)
    time.sleep(5)

def test1():
    b = 0
    while b < 19:
        print(b)
        b = b + 1
        if b % 5 ==0:
            print("gas")

def test2():
    upgradeSDA(sda17,upgradeSDACoord) #ini up wood ke lvl 7
    print("upgradeBuildingTimer: ", upgradeBuildingTimer," selesai")
    upgradeBuildingTimer = upgradeBuildingTimer + 1
        



def main():
    
    # scheduledAutoFarm()

    # collectPop()
    # # upgradeBuilding(townHallCoord,upgradeTownHall)
    # timeFarmCalculator()

    # test1()
    # test2()
    # tempChiefNatar()
    # trainTroops()
    # autoDetect()
    # # click(queueAllSteepeRider4)
    get_cords()
    # click((479 , 604))
    # get_cords_only()
    # mousePos(tempStartingPointForFindGGBCords2)
    # findGGBCords(604,608,230)


    # testtt()
    # waitingTimeUpdate()
    # suicideNatar()
    # GGBValueTest()
    # listPrintCreator()
    
    # timeFarmSchedulingSystem()
    
    # trainTroops()

    
    pass

# spamFlyerPromo()


if __name__ == '__main__':
    main()


# %%(445, 437)(152, 538)
import os

# %%


