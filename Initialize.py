import string
import requests
import json
import codecs
import os
from socket import socket

from Socket import sendMsg
from Settings import loadSettings

def joinRoom(socket):
    readbuffer = ""
    Loading = True
    while Loading:
        readbuffer = readbuffer + socket.recv(1024)
        temp = string.split(readbuffer, "\n")
        readbuffer = temp.pop()

        for line in temp:
            Loading = loadingComplete(line)
    sendMsg(socket, "BRBot has joined chat")

def loadingComplete(line):
    if "End of /NAMES list" in line:
        return False
    else:
        return True