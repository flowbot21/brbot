import json
import codecs
import os

HOST = "irc.chat.twitch.tv"
PORT = 6667

SettingsFile = os.path.join(os.path.dirname(__file__), "Settings.json")

def loadSettings():
    with codecs.open(SettingsFile, encoding="utf-8-sig", mode="r") as f:
        settingsDict = json.load(f, encoding="utf-8")
    return settingsDict