from socket import socket as socket2
import socket as socket1
import Settings

def openSocket():
    settingsDict = Settings.loadSettings()
    s = socket1.socket()
    s.connect((Settings.HOST, Settings.PORT))
    s.send("PASS " + settingsDict['BotPass'] + "\r\n")
    s.send("NICK " + settingsDict['BotName'] + "\r\n")
    s.send("JOIN #" + settingsDict['ChannelName'] + "\r\n")
    return s

def closeSocket(sock):
    sendMsg(sock, "BRBot closed")
    socket2.close(sock)
    print "Bot Closed"

def sendMsg(socket, message):
    settingsDict = Settings.loadSettings()
    messageTemp = "PRIVMSG #" + settingsDict['ChannelName'] + " :" + message
    socket.send(messageTemp + "\r\n")