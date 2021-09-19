from BasicCommands import *

########## Variables  ###########
#region
#endregion

FlyerPromo = 338, 617
FlyerPromoRandom = 311, 589, 343, 624
table1 = 142, 276 #here last
table2 = 214, 266
table3 = 297, 273
table4 = 140, 376
table5 = 219, 372
table6 = 301, 377

stinkCoord = 71, 292
cod1 = 64, 290
codtable1 = 151, 319
codtable2 = 232, 318
codtable3 = 305, 319
codtable4 = 148, 419
codtable5 = 228, 422
codtable6 = 295, 422
cod2 = 191, 521
cod3 = 173, 558
grainCoord = 58, 259
SuperPromote1 = 413, 607
SuperPromote2 = 347, 436

tipsCoord1 = 166, 203
tipsCoord2 = 116, 431
swipeToRight = 349, 350
swipeToLeft = 20, 352

trash1 = 154, 490
trash2 = 186, 382
trash3 = 137, 552
oneHourWarning = 185, 431
specialCustomers = 269, 438



def autoFarmBitch():
    while True:
        time.sleep(1)
        
        spamFlyerPromo()
        takeTips()
        clickAll()          #1
        clickAllKitchen()
        cleanTrash()
        spamFlyerPromo()
        clickAll()          #2
        clickAllKitchen()
        clickWholeBothScreen()
        stink()
        time.sleep(10)
        # time.sleep(100)

def autoFarmBitch2():
    while True:
        time.sleep(1)
        randomSpamFlyerPromo()
        takeFoodOrders()

def stink():
    i = 0
    while i < 40:
        click(stinkCoord)
        time.sleep(0.05)
        i = i + 1

def spamFlyerPromo():
    i = 0
    while i < 120:
        click(FlyerPromo)
        time.sleep(0.05)
        i = i + 1

def randomSpamFlyerPromo():
    global randomClicksLeft
    time.sleep(3) #optional
    while True:
        takeFoodOrders() # Tambahan script
        click(oneHourWarning) # Tambahan script
        click(specialCustomers) # Tambahan script
        i = 0
        randomClicks = random.randint(305,325)
        while i < randomClicks:
            print("click for ",randomClicks - i," times")
            click(randomize(FlyerPromoRandom))
            time.sleep(0.1)
            i = i + 1
            if i % 60 == 0:
                #time.sleep(5) #optional
                takeFoodOrders() # Tambahan script
                click(oneHourWarning) # Tambahan script
                click(specialCustomers) # Tambahan script
        randomTimeSleep = random.randint(3,7)
        print("sleep for ", randomTimeSleep)
        takeFoodOrders() # Tambahan script
        time.sleep(randomTimeSleep)

def clickAll():
    listClick = (
        table1,table2,table3,table4,table5,table6,
        cod1, cod2, cod3,
        codtable1, codtable2, codtable3, codtable4, codtable5, codtable6,
    )
    i = 0
    while i < len(listClick):
        click(listClick[i])
        time.sleep(0.25)
        i = i + 1

def takeFoodOrders():
    listClick = (
        table2,table2,table4,table4,table5,table6,)
    i = 0
    while i < len(listClick):
        click(listClick[i])
        time.sleep(0.25)
        i = i + 1


def takeTips():
    print()
    click(tipsCoord1)
    time.sleep(1)
    click(tipsCoord2)
    time.sleep(1)

def clickAllKitchen():
    listClick =(
        swipeToRight,
        table3,
        grainCoord,cod2,
        swipeToLeft
    )
    i = 0
    while i < len(listClick):
        click(listClick[i])
        time.sleep(0.25)
        i = i + 1
    pass

def cleanTrash():
    listClick =(
        swipeToRight,
        trash1, trash2, trash3,
        swipeToLeft
    )
    i = 0
    while i < len(listClick):
        click(listClick[i])
        time.sleep(0.5)
        i = i + 1
    pass

def clickWholeScreen():
    begCoordx = 234
    begCoordy = 500 #303
    
    while True:
        currentCoord = begCoordx, begCoordy
        click(currentCoord)
        begCoordx = begCoordx + 20
        
        if begCoordx > 300:
            begCoordx = 64
            begCoordy = begCoordy + 20
            time.sleep(0.25)
        if begCoordy > 552:
            begCoordy = 290+130
            time.sleep(1)
            break
    
def clickWholeBothScreen():
    clickWholeScreen()
    click(swipeToRight)
    time.sleep(1)
    clickWholeScreen()
    click(swipeToLeft)
    time.sleep(1)


def main():
    # get_cords()
    # autoFarmBitch()
    # autoFarmBitch2() #bad
    # takeTips()
    # clickWholeScreen()
    randomSpamFlyerPromo()
    pass

# spamFlyerPromo()


if __name__ == '__main__':
    main()


# %%
import os

# %%
