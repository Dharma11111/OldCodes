from BasicCommands import *

def main():
    #mousePos((437,147))
    #RGBValueTest()
    get_cords_only()
    # autoRefreshBrowser()

    # sendRaid()
    
    
        
    pass

def sendRaid():
    click((547,48))
    time.sleep(3)
    farmListLink = "https://ts5.x1.europe.travian.com/build.php?id=39&gid=16&tt=99"
    pastee()
    time.sleep(1)
    enterr()
    time.sleep(5)

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

if __name__ == '__main__':
    main()














#END
