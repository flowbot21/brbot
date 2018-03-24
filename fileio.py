import io
import os
from Socket import sendMsg

soloWins = os.path.join(os.path.dirname(__file__),"SoloWins.txt")
soloList = os.path.join(os.path.dirname(__file__),"SoloList.txt")
duoWins = os.path.join(os.path.dirname(__file__),"DuoWins.txt")
duoList = os.path.join(os.path.dirname(__file__),"DuoList.txt")
squadWins = os.path.join(os.path.dirname(__file__),"SquadWins.txt")
squadList = os.path.join(os.path.dirname(__file__),"SquadList.txt")
totalWins = os.path.join(os.path.dirname(__file__),"TotalWins.txt")

def addWin(wintype, count):
    if wintype == "solo":
        winsName = soloWins
        listName = soloList
    elif wintype == "duo":
        winsName = duoWins
        listName = duoList
    elif wintype == "squad":
        winsName = squadWins
        listName = squadList
    winsRead = open(winsName,"r")
    oldWins = winsRead.readline()
    oldWins_int = int(oldWins)
    winsRead.close()
    newWins = oldWins_int + 1
    winsWrite = open(winsName,"w")
    winsWrite.write('%s' %str(newWins))
    winsWrite.close()
    if oldWins_int == 0:
        listWrite = open(listName,"w")
    else:
        listWrite = open(listName, "a")
    listWrite.write("%i\n" %count)

def resetWins():
    f = open(soloWins,"w")
    f.write("0")
    f.close()

    f = open(soloList,"w")
    f.write("None")
    f.close()

    f = open(duoWins,"w")
    f.write("0")
    f.close()

    f = open(duoList,"w")
    f.write("None")
    f.close()

    f = open(squadWins,"w")
    f.write("0")
    f.close()

    f = open(squadList,"w")
    f.write("None")
    f.close()

    f = open(totalWins,"w")
    f.write("0")
    f.close()

def callWins(socket):
    solowinsRead = open(soloWins,"r")
    duolistRead = open(duoList,"r")
    squadlistRead = open(squadList,"r")
    
    soloWins_str = solowinsRead.readline()
    if soloWins_str.isdigit() == False:
        soloWins_int = 0
    else:
        soloWins_int = int(soloWins_str)
    solowinsRead.close()
    
    duowinsRead = open(duoWins,"r")
    duoWins_str = duowinsRead.readline()
    if duoWins_str.isdigit() == False:
        duoWins_int = 0
    else:
        duoWins_int = int(duoWins_str)
    duowinsRead.close()
    
    squadwinsRead = open(squadWins,"r")
    squadWins_str = squadwinsRead.readline()
    if squadWins_str.isdigit() == False:
        squadWins_int = 0
    else:
        squadWins_int = int(squadWins_str)
    squadwinsRead.close()

    totalWins_int = soloWins_int + duoWins_int + squadWins_int

    sololistRead = open(soloList,"r")
    solowinData = []
    
    for count,z in enumerate(sololistRead.readlines()):
        solowinData.append(z)
        if count > 14:
            break
    sololistRead.close()
            
    duowinData = []
    for count,z in enumerate(duolistRead.readlines()):
        duowinData.append(z)
        if count > 14:
            break
    duolistRead.close()
            
    squadwinData = []
    for count,z in enumerate(squadlistRead.readlines()):
        squadwinData.append(z)
        if count > 14:
            break
    squadlistRead.close()
    
    solowinData = [string.strip("\n") for string in solowinData]
    solowinData = ', '.join(solowinData)
    duowinData = [string.strip("\n") for string in duowinData]
    duowinData = ', '.join(duowinData)
    squadwinData = [string.strip("\n") for string in squadwinData]            
    squadwinData = ', '.join(squadwinData)
    
    if totalWins_int == 0:
        sendMsg(socket, "No wins today")
    elif soloWins_int != 0 and duoWins_int == 0 and squadWins_int == 0:
        sendMsg(socket, "%i Wins (%i Solo: [%s])" %(totalWins_int,soloWins_int,solowinData))
    elif soloWins_int == 0 and duoWins_int != 0 and squadWins_int == 0:
        sendMsg(socket, "%i Wins (%i Duo: [%s])" %(totalWins_int,duoWins_int,duowinData))
    elif soloWins_int == 0 and duoWins_int == 0 and squadWins_int != 0:
        sendMsg(socket, "%i Wins (%i Squad: [%s])" %(totalWins_int,squadWins_int,squadwinData))
    elif soloWins_int != 0 and duoWins_int != 0 and squadWins_int == 0:
        sendMsg(socket, "%i Wins (%i Solo: [%s]; %i Duo: [%s])" %(totalWins_int,soloWins_int,solowinData,duoWins_int,duowinData))  
    elif soloWins_int != 0 and duoWins_int == 0 and squadWins_int != 0:
        sendMsg(socket, "%i Wins (%i Solo: [%s]; %i Squad: [%s])" %(totalWins_int,soloWins_int,solowinData,squadWins_int,squadwinData))
    elif soloWins_int == 0 and duoWins_int != 0 and squadWins_int != 0:
        sendMsg(socket, "%i Wins (%i Duo: [%s]; %i Squad: [%s])" %(totalWins_int,duoWins_int,duowinData,squadWins_int,squadwinData))
    else:
        sendMsg(socket, "%i Wins (%i Solo: [%s]; %i Duo: [%s]; %s Squad: [%s])" %(totalWins_int,soloWins_int,solowinData,duoWins_int,duowinData,squadWins_int,squadwinData))