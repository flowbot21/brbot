import string
import io
import sys
from datetime import datetime, timedelta
import socket
import json

from Socket import openSocket, closeSocket, sendMsg
from Initialize import joinRoom
from Read import getMsg, getUser, getUserLevel
from fileio import addWin, resetWins, callWins
from TRN import getStats, getLastWin

Running = True
sock = openSocket()
joinRoom(sock)
print "Bot Initialized"
readbuffer = ""
sololastUsed = datetime(2018,1,1,00,00,00)
duolastUsed = datetime(2018,1,1,00,00,00)
squadlastUsed = datetime(2018,1,1,00,00,00)
sock.send("CAP REQ :twitch.tv/tags\r\n")
sock.send("CAP REQ :twitch.tv/commands\r\n")
peeTimer = datetime.now()
dadGreeting = True
while Running:
    readbuffer = readbuffer + sock.recv(1024)
    temp = string.split(readbuffer, "\n")
    readbuffer = temp.pop()
    
    peeCheck = datetime.now() - (peeTimer + timedelta(seconds = 3600))
    if peeCheck > timedelta(seconds = 0):
        sendMsg(sock, "@cookeeeemonster it's time for a pee break")
        peeTimer = datetime.now()
    for line in temp:
        if "PING :tmi.twitch.tv" in line:
            sock.send("PONG :tmi.twitch.tv\r\n")
            print "Connection Refreshed %s" %datetime.now()
        elif ":tmi.twitch.tv CAP * ACK :twitch.tv/tags" in line:
            message = ""
        elif ":tmi.twitch.tv CAP * ACK :twitch.tv/commands" in line:
            message = ""
        else:
            user = getUser(line)
            message = getMsg(line)
            user_level = getUserLevel(line)

            if message.startswith("!addwin"):
                if user_level == "broadcaster" or user_level == "moderator" or user == "golden_eagle_gaming":
                    separate = message.split(" ", 2)
                    winType = separate[1]
                    count = int(separate[2])
                    if winType == "solo":
                        cooldownCheck = datetime.now() - (sololastUsed + timedelta(seconds = 15))
                        if cooldownCheck > timedelta(seconds = 0):
                            addWin("solo", count)
                            sendMsg(sock, "Solo Win Added (%s Kills)" %count)
                            sololastUsed = datetime.now()
                        else:
                            sendMsg(sock, "Command is still on cooldown")
                    elif winType == "duo":
                        cooldownCheck = datetime.now() - (duolastUsed + timedelta(seconds = 15))
                        if cooldownCheck > timedelta(seconds = 0):
                            addWin("duo", count)
                            sendMsg(sock, "Duo Win Added (%s Kills)" %count)
                            duolastUsed = datetime.now()
                        else:
                            sendMsg(sock, "Command is still on cooldown")
                    elif winType == 'squad':
                        cooldownCheck = datetime.now() - (squadlastUsed + timedelta(seconds = 15))
                        if cooldownCheck > timedelta(seconds = 0):
                            addWin("squad", count)
                            sendMsg(sock, "Squad Win Added (%s Kills)" %count)
                            squadlastUsed = datetime.now()
                        else:
                            sendMsg(sock, "Command is still on cooldown")
                    else:
                        sendMsg(sock, "Invalid Win Type")
            elif message.startswith("!resetwins"):
                if user_level == 'broadcaster' or user_level == 'moderator' or user == "golden_eagle_gaming":
                    resetWins()
                    sendMsg(sock, "Wins Reset")

            elif message.startswith("!wins"):
                callWins(sock)
            
            elif message.startswith("!closebot"):
                if user_level == 'broadcaster' or user_level == 'moderator' or user == "golden_eagle_gaming":
                    closeSocket(sock)
                    sys.exit()
            elif message.startswith("!fortnite"):
                separate = message.split(" ", 3)
                if len(separate) >=4:
                    touser = separate[1]
                    stat = separate[2]
                    platform = separate[3]
                    printMessage = getStats(user, stat, touser, platform)
                    sendMsg(sock, "%s" %printMessage)
            elif message.startswith("!lastwin") and user_level == 'broacaster' or user_level == 'moderator':
                lastKills = getLastWin()
                if lastKills == False:
                    sendMsg(sock, "No wins in last 10 games")
                else:
                    sendMsg(sock, "Kills Last Win: %s" %lastKills)