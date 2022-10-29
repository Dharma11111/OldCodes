from decimal import ROUND_DOWN
from random import randint
from BasicCommands import *
from pullAndParseToMainLogic import *
from StringManipulation import *
# from ZZZcollectData import *

###########################################################################
# VSCode ShortCuts
#region

#fold All = Ctrl + K, Ctrl + 0  --> itu angka nol

#endregion

###########################################################################
# Variables
#region 
###########################################################################

# Google Chrome aligned on Top-Left
# Chrome resized so that chrome elements stay static
# zoom level 100%



# Global Variable
rawData = 0




###########################################################################
# Program's Link
idleParsingDataCoord = 798,921
mozilaFirefox = 218, 1055
playMozilaYoutubeVideo = 591, 418
googleChrome = 268, 1060

firstTabChrome = 98,21
secondTabChrome = 363, 25
hangoutsGoogleCallButtom = 823,204
hangoutsGoogleCallStart = 934,315
hangoutsGoogleCallStop = 967,917

###########################################################################
farmListLink = "https://ts6.x1.asia.travian.com/build.php?id=39&gid=16&tt=99"
browserUrlCoord = 547,55

sendRaidCoord1 = 830,421 #applied # there's "Beginner Protection Notice"
sendRaidCoord2 = 826,536 
sendRaidCoord3 = 826,651 

sdaPageUrl = "https://ts6.x1.asia.travian.com/dorf1.php"

clubsAmountCoord = 410,377 #full screen
#clubsAmountCoord2 = 407,377 #non full screen

#spearAmountCoord = 413,407 #non full screen
#paladinAmountCoord = 547,409 #non full screen
#ramAmountCoord = 697,375 #non full screen

chooseAttackModeCoord = 612,509 #full screen
#chooseAttackModeCoord2 = 612,508  #non full screen (Y lebih besar 9)

chooseRaidModeCoord = 611,531 #full screen

confirmAttackCoord = 870,563  #full screen
#confirmAttackCoord2 = 875,553 #non full screen

# Incoming Attack
    # RGB Values incoming attack merah (212,0,0) Total RGB Values = 212 
    # Alternative Coord yang RGB nya 212 adalah (784,282), (780,282), (771,282)
IncomingAttackRGBCoord = 789,282 

# Village link Coord
    # Jarak antara village link sekitar 20 pixel Y
Village1X = 1030
Village1Y = 455 #range Y adalah 445 sampai 465
UrlVillage1 = "https://ts6.x1.asia.travian.com/dorf1.php?newdid=19528&" # New Village
Village2 = 1030, 475 #range Y adalah 466 sampai 487
UrlVillage2 = "https://ts6.x1.asia.travian.com/dorf1.php?newdid=17422&"


###########################################################################
# Building Links
barracksUrl = "https://ts6.x1.asia.travian.com/build.php?id=35&gid=19"
#stableUrl = "https://ts6.x1.europe.travian.com/build.php?id=34&gid=20"


maxAmountPhalanxCoordX = 640        # 2 clicking points to activate rapidlyShiftingClick
maxAmountPhalanxCoordY = 550        # +75


trainPhalanxCoordX = 400        # 400
trainPhalanxCoordY = 660        # +80


#endregion


###########################################################################
# Oasis Links
#region 
# Close Distance Oasis
#zl = "LINK                                                                                 "   
#zt = Raiding Cooldown (seconds) # Oasis Coord

oasis1 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=85242"
oasis2 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=86046"
oasis3 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=84841"
oasis4 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=84439"
oasis5 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=84839"
oasis6 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=87249"
oasis7 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=84838"
oasis8 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=86442"
oasis9 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=87252"
oasis10 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=83635"
oasis11 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=84035"
oasis12 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=82436"
oasis13 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=84850"
oasis14 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=85638"
oasis15 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=85652"
oasis16 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=82834"
oasis17 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=83646"
oasis18 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=87646"
oasis19 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=84851"
oasis20 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=82034"
oasis21 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=88853"
oasis22 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=84852"
oasis23 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=82431"
oasis24 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=82041"
oasis25 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=81638"
oasis26 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=86456"
oasis27 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=88058"
oasis28 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=88859"
oasis29 = "https://ts6.x1.asia.travian.com/build.php?gid=16&tt=2&eventType=4&targetMapId=88444"


# Far Distance Oasis 


# Potentially High Yield Farm
# 15 | -19 

# oasisLinkList = [0,zl8,zl9,zl10,zl3,zl1,zl2,zl4,zl5,zl6,zl7]
oasisLinkList   = [0,oasis1,oasis2,oasis3,oasis4,oasis5
                    ,oasis6,oasis7,oasis8,oasis9,oasis10
                    ,oasis11,oasis12,oasis13,oasis14,oasis15
                    ,oasis16,oasis17,oasis18,oasis19,oasis20
                    ,oasis21,oasis22,oasis23,oasis24,oasis25
                    ,oasis26,oasis27,oasis28,oasis29]
oasisTimeList = []
FARoasisLinkList= []

#endregion

###########################################################################
# Code Functions

def main():
    # testCode("lol","haha","wow")
    # mousePos((640,550))
    # RGBValueTest()
    # get_cords_only()
    # rapidlyShiftingRGBValue(760,819,282)
    # rapidlyShiftingGet_cords_only(1030,434,493)

    JARVIS(60*4,999999,60*10,60*12)
    # scanIncomingAttack(3)


    pass

#region 

def testCode(x,y,z):
    print(x)
    testCode2(y,z)
    asd = 100
    fgh = 100
    pass

def testCode2(y,z):
    print(y)
    print(z)
    pass


def cleanInt(variable):
    clean = ''.join(c for c in variable if c.isdigit()) ##    print(clean)
    return int(clean)

def findDataIndex(keyword):
    global rawData
    rawData = singleLineParse()
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print (rawData.find(keyword))
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return rawData.find(keyword)


def trainTroops( buildingType, mouseScrollAmount, troopsTypeX, troopsTypeY, trainTroopsCoordX, trainTroopsCoordY ):
    i = 0
    click(browserUrlCoord)
    time.sleep(1)
    write(buildingType)      # barracksUrl, stableUrl
    time.sleep(1)
    enterr()
    time.sleep(5)
    click(chooseAttackModeCoord) # click on empty screen, to enable mouse scroll
    
    while i < mouseScrollAmount: # Scroll phalanx 3x, 
        time.sleep(0.5)
        mouseScrollDown()  # scroll down for mouseScrollAmount times
        time.sleep(0.5)
        i += 1
    print("Training Troops") 
    fullScreenGrab()
    
    rapidlyShiftingClick1(troopsTypeX,troopsTypeY,troopsTypeY+75)                    # maxAmountPhalanxCoord # write the bigger Y first then the smaller Y, to prevent pressing gold builder
    time.sleep(1)
    rapidlyShiftingClick1(trainTroopsCoordX,trainTroopsCoordY,trainTroopsCoordY+80)  # trainPhalanxCoord     # 
    time.sleep(1)


def activateDataParse():
    click(idleParsingDataCoord)
    time.sleep(1)
    ff5()

def getAmountOfTroops():
    global rawData
    AA = findDataIndex("Legionnaires")
    if AA == -1:
        print("Troops not found")
        return 0
    else:
        print(rawData[AA:AA+16])            # Kalau "Phalanxes"     -> AA + 13
        print(rawData[AA+13:AA+15])         # Kalau "Legionnaires"  -> AA + 16 karena 3 huruf lebih banyak
        phalanxAvailable = cleanInt(rawData[AA+13:AA+15])          #-> ini harus adjust juga AA + X
        return phalanxAvailable

def openSdaPage():
    click(browserUrlCoord)
    time.sleep(1)
    write(sdaPageUrl)
    time.sleep(1)
    enterr()
    time.sleep(3)

def countDown(description, duration1,duration2):
    duration = randint(duration1,duration2)
    while 1<duration:
        time.sleep(1)
        print(description, duration)
        duration = duration-1

def countUp(currentTimer):
    i = currentTimer
    # print(i)
    i = i+1
    time.sleep(1)
    return i

def autoRefreshBrowser():
    while 1<5:
        get_cords_only()
        
        mousePos((89,50))
        leftClick()

        time.sleep(2)

        mousePos((717,196))
        leftClick()

        #mousePos((1083,660)) #tombol register
        #leftClick()
        
        if 765 != RGBValueTest():
            print("loading!")
            mousePos((266,601))
            leftClick()
            mousePos((425,280))
            leftClick()
            pass
        
        i = 0
        while i < 10:
            time.sleep(1)
            print(10-i)
            i = i+1

def scanIncomingAttack(numberOfVillages):
    i = 0
    while i < numberOfVillages:

        click(browserUrlCoord)
        time.sleep(0.5)
        write(sdaPageUrl)
        enterr()
        time.sleep(3)

        XCoord = Village1X
        YCoord = Village1Y + i * 20  # Jarak antar link village itu 20 pixel Y
        click((XCoord,YCoord))

        # if confirmRGBValue(IncomingAttackRGBCoord) == 212:   #Ini bisa dipake kalau aku lg di Jambi
        #     print("There is an incoming attack") 
        #     click(mozilaFirefox)
        #     time.sleep(1)
        #     click(playMozilaYoutubeVideo)
        #     time.sleep(1)
        #     click(googleChrome)

        if confirmRGBValue(IncomingAttackRGBCoord) == 212:      #Google Hangouts ada di second tab chrome
            print("There is an incoming attack")                #Target call ke dickydharma17@gmail.com
            while True:
                click(secondTabChrome)                              #chat box sudah terbuka di sudut kanan bawah layar
                time.sleep(1)
                click(hangoutsGoogleCallButtom)
                time.sleep(1)
                click(hangoutsGoogleCallStart)
                time.sleep(20)
                click(hangoutsGoogleCallStop)
                time.sleep(1)
        else:
            print("account is safe")
        i += 1

def sendRaidd(raidCooldownMin,raidCooldownMax):
    click(browserUrlCoord)
    time.sleep(1)
    write(farmListLink)
    time.sleep(1)
    enterr()
    time.sleep(5)
    click(sendRaidCoord1)
    time.sleep(2)
    click(sendRaidCoord2)
    time.sleep(2)
    click(sendRaidCoord3)
    countDown("Raid cooldown: ",raidCooldownMin,raidCooldownMax)

#endregion

###########################################################################
# Gold Club Functions

def JARVIS(initiateTime,troopsTrainingFrequency,raidCooldownMin,raidCooldownMax):
    countDown("initiate time: ",initiateTime,initiateTime+1)  # wait before sending raid
    troopsTypeCounter = 1

    while True:
        scanIncomingAttack(3)
        sendRaidd(raidCooldownMin,raidCooldownMax)
        if troopsTypeCounter % troopsTrainingFrequency == 0:
            trainTroops(barracksUrl,3,maxAmountPhalanxCoordX,maxAmountPhalanxCoordY,trainPhalanxCoordX,trainPhalanxCoordY)
        # else:
        #     trainTroops(barracksUrl, 4, maxAmountPhalanxCoord, trainPhalanxCoord)
        troopsTypeCounter += 1
        
        


###########################################################################
# Pre Gold Club Functions
#region

# def main():
#     time.sleep(3)
#     raidOasisSchedule(oasisLinkList)
#     get_cords_only()
#     collectOasisUrlToGsheet()
#     writeOasisUrlFromGsheetToNotepad()
#     pass

def raidOasis(oasisURL):    # early game raiding oasis using phalanx
                            # time needed to execute this loop is xxx seconds
    click(browserUrlCoord)
    time.sleep(0.5)
    write(oasisURL)
    enterr()
    time.sleep(2)
    click(clubsAmountCoord)
    time.sleep(0.5)
    write("2")
    time.sleep(0.1)
    enterr()
    time.sleep(2)
    click(confirmAttackCoord)
    time.sleep(1)

def raidOasisSchedule(raidList):                    # manual Link raid before Gold Club
    timer = 0
    timerActive = 1#+60*35                           # timer the first raid
    numberOfPossibleRaidParsed = 0
    while True:
        try:
            timer = countUp(timer)
            print(timer,"---",timerActive)
            
            if timer % timerActive == 0:
                numberOfPossibleRaidParsed =  parsingTroopsAmount(raidList)

            while numberOfPossibleRaidParsed > 0:   # Send raid based of how many raids are possible 
                raidOasis(raidList[numberOfPossibleRaidParsed])
                print("Raiding Oasis Number: ",numberOfPossibleRaidParsed)
                numberOfPossibleRaidParsed -= 1

            if timer % timerActive == 0:
                # continue
                trainOrNot =  0#randint(0,1)
                if trainOrNot == 1:
                    trainTroops(barracksUrl,3,maxAmountPhalanxCoordX,maxAmountPhalanxCoordY,trainPhalanxCoordX,trainPhalanxCoordY)
                     
                else:
                    print("Not Training Troops")

                timerActive = timer + randint(60*45,60*50)    # timer send raid
                print("timerActive: ",timerActive)
            
        except ValueError:
            print("error")
            timerActive = timer + randint(60*30,60*35)    # timer send raid
            print("timerActive: ",timerActive)
            continue
            
def parsingTroopsAmount(raidList):
    
    print("parsing troops amount")
    openSdaPage()
    activateDataParse()
    amountOfTroops = getAmountOfTroops()
    print(amountOfTroops)
    numberOfPossibleRaid = math.floor(amountOfTroops/2)
    print("numberOfPossibleRaid: ",numberOfPossibleRaid)
    if numberOfPossibleRaid > len(raidList)-1:  #the limit of raid target
        numberOfPossibleRaid = len(raidList)-1

    return  numberOfPossibleRaid

def collectOasisUrlToGsheet():
    googleChromeEmptySpace1 = 743,20
    googleChromeEmptySpace2 = 1713,20
    click(googleChromeEmptySpace1)
    time.sleep(0.2)

    while True:
        click(browserUrlCoord)
        time.sleep(0.2)
        copyy()
        time.sleep(0.2)
        click(googleChromeEmptySpace2)
        time.sleep(0.2)
        pastee()
        time.sleep(0.2)
        arrowDownn()
        time.sleep(0.2)
        click(googleChromeEmptySpace1)
        time.sleep(0.2)
        ctrlTabb()
        time.sleep(0.2)

    pass

def writeOasisUrlFromGsheetToNotepad():  #Link URL yang SUDAH DI SORT berdasarkan distance dipindah ke Notepad
    googleChromeEmptySpace1 = 743,20
    googleChromeEmptySpace2 = 1713,20
    oasisCount = 1

    click(googleChromeEmptySpace1)
    time.sleep(0.2)

    while True:
        copyy()
        time.sleep(0.05)
        click(googleChromeEmptySpace2)
        time.sleep(0.05)
        write("oasis")
        write(oasisCount)
        write(' = "')
        time.sleep(0.05)
        pastee()
        time.sleep(0.05)
        write('"')
        time.sleep(0.05)
        enterr()
        time.sleep(0.05)
        click(googleChromeEmptySpace1)
        time.sleep(0.05)
        arrowDownn()
        time.sleep(0.05)
        oasisCount +=1
    pass


def trollRaid():                            # manual Link raid before Gold Club
    i = 0
    while True:  
        click(browserUrlCoord)
        time.sleep(0.5)
        write(crepsVillageCoord)
        enterr()
        time.sleep(2)

        print("i = ",i)
        if i < 2:
            click(clubsAmountCoord)
        elif i < 30:
            click(paladinAmountCoord)
        elif i < 46:
            click(spearAmountCoord)
        elif i < 52:
            click(ramAmountCoord)
        else:
            break
        i = i+1

        time.sleep(0.5)
        write("1")
        click(chooseAttackModeCoord2)
        enterr()
        time.sleep(2)
        click(confirmAttackCoord2)
        countDown("Raid cooldown: ",2,5)

#endregion

if __name__ == '__main__':
    main()














#END
