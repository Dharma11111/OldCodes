##from ZZZcollectData import *
# Costs of buildings #

#*** SDA coords
UrlBoxChrome = [250 , 55]
SDAUpgradeButton = [552 , 688]
##### Type Village    # 4446
sda0   =[470,317]   # wood
sda1   =[587-30 , 324]   # crop
sda2   =[662-30 , 330]   # wood
sda3   =[425-30 , 359]   # iron
sda4   =[556-30 , 368]   # clay
sda5   =[614-30 , 375]   # clay
sda6   =[709-30 , 378]   # iron
sda7   =[380-30 , 407]   # crop
sda8   =[458-30 , 406]   # crop
sda9   =[673-30 , 400]   # iron
sda10  =[756-30 , 397]   # iron
sda11  =[380-30 , 464]   # crop
sda12  =[461-30 , 455]   # crop
sda13  =[721-30 , 459]   # crop
sda14  =[589-30 , 490]   # wood
sda15  =[479-30 , 540]   # clay
sda16  =[564-30 , 540]   # wood
sda17  =[667-30 , 527]   # clay

#*** Building coords

building0   =[585-30 , 301]
building1   =[698-30 , 283]
building2   =[811-30 , 306]
building3   =[760-30 , 351]
building4   =[698-30 , 411]
building5   =[845-30 , 419] # RallyPoint
building6   =[910-30 , 355]
building7   =[940-30 , 417]
building8   =[945-30 , 496]
building9   =[871-30 , 576]
building10  =[784-30 , 530]
building11  =[777-30 , 603]
building12  =[657-30 , 613]
building13  =[645-30 , 538]
building14  =[550-30 , 604]
building15  =[450-30 , 545]
building16  =[549-30 , 477]
building17  =[428-30 , 480]
building18  =[436-30 , 414]
building19  =[548-30 , 403] # MainBuilding
building20  =[479-30 , 344]
building21  =[694-30 , 657] # Wall


#*** SDA Upgrade Cost

woodTo1  = ['40', '100', '50', '60']
woodTo2  = ['65', '165', '85', '100']
woodTo3  = ['110', '280', '140', '165']
woodTo4  = ['185', '465', '235', '280']
woodTo5  = ['310', '780', '390', '465']
woodTo6  = ['520', '1300', '650', '780']
woodTo7  = ['870', '2170', '1085', '1300']
woodTo8  = ['1450', '3625', '1810', '2175']
woodTo9  = ['2420', '6050', '3025', '3630']
woodTo10 = ['4040', '10105', '5050', '6060']


clayTo1  = ['80', '40', '80', '50']
clayTo2  = ['135', '65', '135', '85']
clayTo3  = ['225', '110', '225', '140']
clayTo4  = ['375', '185', '375', '235']
clayTo5  = ['620', '310', '620', '390']
clayTo6  = ['1040', '520', '1040', '650']
clayTo7  = ['1735', '870', '1735', '1085']
clayTo8  = ['2900', '1450', '2900', '1810']
clayTo9  = ['4840', '2420', '4840', '3025']
clayTo10 = ['8080', '4040', '8080', '5050']

ironTo1  = ['100', '80', '30', '60']
ironTo2  = ['165', '135', '50', '100']
ironTo3  = ['280', '225', '85', '165']
ironTo4  = ['465', '375', '140', '280']
ironTo5  = ['780', '620', '235', '465']
ironTo6  = ['1300', '1040', '390', '780']
ironTo7  = ['2170', '1735', '650', '1300']
ironTo8  = ['3625', '2900', '1085', '2175']
ironTo9  = ['6050', '4840', '1815', '3630']
ironTo10 = ['10105', '8080', '3030', '6060']

cropTo1  = ['70', '90', '70', '20']
cropTo2  = ['115', '150', '115', '35']
cropTo3  = ['195', '250', '195', '55']
cropTo4  = ['325', '420', '325', '95']
cropTo5  = ['545', '700', '545', '155']
cropTo6  = ['910', '1170', '910', '260']
cropTo7  = ['1520', '1950', '1520', '435']
cropTo8  = ['2535', '3260', '2535', '725']
cropTo9  = ['4235', '5445', '4235', '1210']
cropTo10 = ['7070', '9095', '7070', '2020']

#*** Building Upgrade Cost

heroMansionTo1  = ['700', '670', '700', '240']
heroMansionTo2  = ['930', '890', '930', '320']
heroMansionTo3  = ['1240', '1185', '1240', '425']
heroMansionTo4  = ['1645', '1575', '1645', '565']
heroMansionTo5  = ['2190', '2095', '2190', '750']
heroMansionTo6  = ['2915', '2790', '2915', '1000']
heroMansionTo7  = ['3875', '3710', '3875', '1330']
heroMansionTo8  = ['5155', '4930', '5155', '1765']
heroMansionTo9  = ['6855', '6560', '6855', '2350']
heroMansionTo10 = ['9115', '8725', '9115', '3125']
heroMansionTo11 = ['12125', '11605', '12125', '4155']
heroMansionTo12 = ['16125', '15435', '16125', '5530']
heroMansionTo13 = ['21455', '20525', '21445', '7350']
heroMansionTo14 = ['28520', '27300', '28520', '9780']
heroMansionTo15 = ['37935', '36310', '37935', '13005']
heroMansionTo16 = ['50450', '48290', '50450', '17300']
heroMansionTo17 = ['67100', '64225', '67100', '23005']
heroMansionTo18 = ['89245', '85420', '89245', '30600']
heroMansionTo19 = ['118695', '113605', '118695', '40695']
heroMansionTo20 = ['157865', '151095', '157865', '54125']


"""

"""









# Code untuk collect data dari excel

def aaa1():       #*** Automate buat list Data
    i = 0
    while i < 10:
        print("heroMansionTo",i,"  = ",sep='')
        i=i+1
    while i < 21:
        print("heroMansionTo",i," = ",sep='')
        i=i+1
    pass

rawData = ""
def aaaparse():
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
    print (resultt)
    return resultt 
    
################################ TEST AREA #############################################


############################################
def aaa2():           #***  Olah hasil parse buat dipake di a3
    global rawData
    rawData = rawData.split("\t")
    print(rawData)

def aaa3():           #***   kasih \n supaya rapi
    global rawData
    rawDataa = "['700', '670', '700', '240\n930', '890', '930', '320\n1240', '1185', '1240', '425\n1645', '1575', '1645', '565\n2190', '2095', '2190', '750\n2915', '2790', '2915', '1000\n3875', '3710', '3875', '1330\n5155', '4930', '5155', '1765\n6855', '6560', '6855', '2350\n9115', '8725', '9115', '3125\n', '', '', '\n12125', '11605', '12125', '4155\n16125', '15435', '16125', '5530\n21455', '20525', '21445', '7350\n28520', '27300', '28520', '9780\n37935', '36310', '37935', '13005\n', '', '', '\n50450', '48290', '50450', '17300\n67100', '64225', '67100', '23005\n89245', '85420', '89245', '30600\n118695', '113605', '118695', '40695\n157865', '151095', '157865', '54125\n=']"
    
    print(rawDataa)
            
def aaa4():
    time.sleep(5)
    keyboard.type("https://ts6.anglosphere.travian.com/build.php?id=39&gid=16&tt=99")

def main():

##    parse()
##    aaa2()
##    aaa1()
##    aaa3()
    aaa4()
 
if __name__ == '__main__':
    main()
