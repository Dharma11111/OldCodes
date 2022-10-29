from decimal import ROUND_DOWN
from random import randint
from BasicCommands import *

####################################################
#Variables
#region

# H1
# cesg    = 1171
# csize   = -58572
# clev    = -53177
# cslack  = -231007
# cprof   = 189549
# cliq    = 31880
# cvola   = -39410
# cret    = 92532
# closs   = 5176
# cdiv    = -6517

# pesg    = 88
# psize   = 0
# plev    = 15
# pslack  = 23
# pprof   = 9
# pliq    = 1
# pvola   = 271
# pret    = 90
# ploss   = 523
# pdiv    = 400

# coefList = [cesg,csize,clev,cslack,cprof,cliq,cvola,cret,closs,cdiv]
# pList = [pesg,psize,plev,pslack,pprof,pliq,pvola,pret,ploss,pdiv]
# varNameFull = ["tingkat implementasi CSR","firm size","leverage","slack","profitabilitas","likuiditas","volatilitas","stock return","net loss","dividen"]
# varNameShort= ["ESG","SIZE","LEV","SLACK","PROF","LIQ","VOLA","RET","LOSS","DIV"]

#H2 tahap 1
# cesg    = 810
# csize   = -21043
# clev    = -7865
# cslack  = 131750
# cprof   = 19309
# cliq    = 14639
# cvola   = 38626
# cret    = 23540
# closs   = -12736
# cdiv    = 576

# pesg    = 84
# psize   = 175
# plev    = 797
# pslack  = 67
# pprof   = 83
# pliq    = 0
# pvola   = 518
# pret    = 831
# ploss   = 50
# pdiv    = 941

# coefList = [cesg,csize,clev,cslack,cprof,cliq,cvola,cret,closs,cdiv]
# pList = [pesg,psize,plev,pslack,pprof,pliq,pvola,pret,ploss,pdiv]
# varNameFull = ["tingkat implementasi CSR","firm size","leverage","slack","profitabilitas","likuiditas","volatilitas","stock return","net loss","dividen"]
# varNameShort= ["ESG","SIZE","LEV","SLACK","PROF","LIQ","VOLA","RET","LOSS","DIV"]

#H2 tahap 2
cesg    = 972
ccovid  = -3485
csize   = -17959
clev    = -7367
cslack  = 136980
cprof   = -26532
cliq    = 14604
cvola   = 44503
cret    = 25257
closs   = -13003
cdiv    = -1

pesg    = 69
pcovid  = 538
psize   = 183
plev    = 808
pslack  = 74
pprof   = 585
pliq    = 0
pvola   = 494
pret    = 813
ploss   = 47
pdiv    = 1

coefList = [cesg,ccovid,csize,clev,cslack,cprof,cliq,cvola,cret,closs,cdiv]
pList = [pesg,pcovid,psize,plev,pslack,pprof,pliq,pvola,pret,ploss,pdiv]
varNameFull = ["tingkat implementasi CSR","covid","firm size","leverage","slack","profitabilitas","likuiditas","volatilitas","stock return","net loss","dividen"]
varNameShort= ["ESG","COVID","SIZE","LEV","SLACK","PROF","LIQ","VOLA","RET","LOSS","DIV"]


#H2 tahap 3
# cesg    = 931
# ccovid  = -6896
# cesgcovid =84
# csize   = -17134
# clev    = -8224
# cslack  = 137178
# cprof   = -28861
# cliq    = 14627
# cvola   = 45951
# cret    = 25839
# closs   = -12832
# cdiv    = 19

# pesg    = 87
# pcovid  = 681
# pesgcovid =808
# psize   = 160
# plev    = 787
# pslack  = 75
# pprof   = 577
# pliq    = 0
# pvola   = 493
# pret    = 807
# ploss   = 44
# pdiv    = 998

# coefList = [cesg,ccovid,cesgcovid,csize,clev,cslack,cprof,cliq,cvola,cret,closs,cdiv]
# pList = [pesg,pcovid,pesgcovid,psize,plev,pslack,pprof,pliq,pvola,pret,ploss,pdiv]
# varNameFull = ["tingkat implementasi CSR","covid","moderasi covid","firm size","leverage","slack","profitabilitas","likuiditas","volatilitas","stock return","net loss","dividen"]
# varNameShort= ["ESG","COVID","ESGCOVID","SIZE","LEV","SLACK","PROF","LIQ","VOLA","RET","LOSS","DIV"]
#endregion



#region

def significantCheck(pListValue):
    if pListValue > 100:
        valueBooleanReturn = "tidak "
    else:
        valueBooleanReturn = ""

    return valueBooleanReturn

def perolehanLevel(pListValue):
    
    if pListValue < 10:
        perolehanReturn = "pada perolehan P ≥ 0,01 "
        return perolehanReturn
    elif pListValue < 50:
        perolehanReturn = "pada perolehan P ≥ 0,05 "
    else:
        perolehanReturn = ""


    return perolehanReturn

def coefficient(coefValue):
    coefReturn = ""
    coefInt = coefValue / 10000
    leftComma = roundDown(coefInt)
    rightComma = int(round(abs(coefInt - leftComma),4)*10000)
    

    # print(coefInt)
    # print(coefValue)
    # print(leftComma)
    # print(rightComma)
    if rightComma < 10:
        coefReturn = str(leftComma) + ",000" + str(rightComma)
    elif rightComma < 100:
        coefReturn = str(leftComma) + ",00" + str(rightComma)
    elif rightComma < 1000:
        coefReturn = str(leftComma) + ",0" + str(rightComma)
    elif rightComma < 10000:
        coefReturn = str(leftComma) + "," + str(rightComma)
    
    return coefReturn

def pVal(pValue):
    pReturn = ""
    pInt = pValue / 10000
    leftComma = roundDown(pInt)
    rightComma = int(round(abs(pInt - leftComma),4)*10000)
    if rightComma < 10:
        pReturn = str(leftComma) + ",00" + str(rightComma)
    elif rightComma < 100:
        pReturn = str(leftComma) + ",0" + str(rightComma)
    elif rightComma < 1000:
        pReturn = str(leftComma) + "," + str(rightComma)
    
    return pReturn




#endregion

def writeSentence():
    i = 0
    while i < len(pList):

        #untuk H2 harus ganti jadi "tingkat perubahan financial distress"
        sentence = "Variabel " + varNameFull[i] + " (" + varNameShort[i] + \
            ") " + significantCheck(pList[i]) + \
            "memiliki hubungan signifikan " + perolehanLevel(pList[i]) + \
            "terhadap tingkat perubahan financial distress dengan koefisien " + \
            coefficient(coefList[i]) + " dan nilai P " + pVal(pList[i]) +". "
        write(sentence)
        i +=1
    
def writeTable():
    i = 1 #start dari 1 untuk skip esg
    while i < len(pList):
        # write(coefficient(coefList[i]))
        write(perolehanLevel(pList[i]))
        arrowDownn()
        i += 1





def main():
    

    time.sleep(2)
    writeSentence()
    # writeTable()

    # print(len(coefList),\
    # len(pList),\
    # len(varNameFull),\
    # len(varNameShort))

    # a = "Z𝑖𝑡 = 40,7115 + 0,0815 ESG𝑖𝑡 - 2,2898 SIZE𝑖𝑡 - 9,2991 LEV𝑖𝑡 - 4,8792 SLACK𝑖𝑡 + 4,5941 RNDI𝑖𝑡 + 4,5941 PROF𝑖𝑡 - 0,7834 LOSS𝑖𝑡 + 0,2627 LIQ𝑖𝑡 + 5,4839 VOLA𝑖𝑡 - 7,1039 RET𝑖𝑡 - 0,1272 DIV𝑖𝑡 + ∑YEAR𝑖𝑡 + ε𝑖𝑡 "
    # write(a)
    pass











if __name__ == '__main__':
    main()
