from BasicCommands import *

########## Variables  ###########
FlyerPromo = 475 , 605
table1 = 300, 284
table2 = 375, 283
table3 = 445, 280
table4 = 301, 380
table5 = 374, 379
table6 = 447, 378

stinkCoord = 243, 310
cod1 = 234, 303
codtable1 = 320, 326
codtable2 = 385, 325
codtable3 = 459, 325
codtable4 = 313, 429
codtable5 = 388, 419
codtable6 = 457, 411
cod2 = 333, 503
cod3 = 314, 556
grainCoord = 218, 266
SuperPromote1 = 413, 607
SuperPromote2 = 347, 436

tipsCoord1 = 321, 226
tipsCoord2 = 297, 430
swipeToRight = 490, 355
swipeToLeft = 196, 359

trash1 = 316, 506
trash2 = 347, 528
trash3 = 342, 482
trash4 = 0

def autoFarmBitch():
    while True:
        
        # stink()
        spamFlyerPromo()
        takeTips()
        clickAll()          #1
        clickAllKitchen()
        cleanTrash()
        # spamFlyerPromo()
        clickAll()          #2
        clickAllKitchen()
        clickWholeBothScreen()
        time.sleep(5)

def stink():
    i = 0
    while i < 40:
        click(stinkCoord)
        time.sleep(0.05)
        i = i + 1

def spamFlyerPromo():
    i = 0
    while i < 250:
        click(FlyerPromo)
        time.sleep(0.05)
        i = i + 1

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
    
def takeTips():
    print()
    click(tipsCoord1)
    time.sleep(0.25)
    click(tipsCoord2)
    time.sleep(0.25)

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
        time.sleep(0.25)
        i = i + 1
    pass

def clickWholeScreen():
    begCoordx = 234
    begCoordy = 500 #303
    
    while True:
        currentCoord = begCoordx, begCoordy
        click(currentCoord)
        begCoordx = begCoordx + 20
        
        if begCoordx > 460:
            begCoordx = 234
            begCoordy = begCoordy + 20
            time.sleep(0.25)
        if begCoordy > 559:
            begCoordy = 303
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
    autoFarmBitch()
    # takeTips()
    # clickWholeScreen()
    pass

# spamFlyerPromo()


if __name__ == '__main__':
    main()