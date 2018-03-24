import requests
import json
import ast
import string

from Settings import loadSettings

headers = {
    'TRN-Api-Key' : 'fe58e8b5-2536-4579-9726-cf4c34a48fbc'
}

def getStats(user, stat, touser, platform):
    platform = platform.strip('\r')
    response = requests.get("https://api.fortnitetracker.com/v1/profile/%s/%s" %(platform, touser), headers = headers)
    dataDict = ast.literal_eval(response.text)
    if stat == 'solokd' or stat == 'solokills' or stat == 'solowins':
        lifeStats = dataDict['stats']['p2']
        currentStats = dataDict['stats']['curr_p2']
        if stat == 'solokd':
            statString = "@%s %s's Solo K/D: %s (Current Season: %s)" %(user, touser, lifeStats['kd']['value'], currentStats['kd']['value'])
        if stat == 'solokills':
            statString = "@%s %s's Solo Kills: %s (Current Season: %s)" %(user, touser, lifeStats['kills']['value'], currentStats['kills']['value'])
        if stat == 'solowins':
            statString = "@%s %s's Solo Wins: %s (Current Season: %s)" %(user, touser, lifeStats['top1']['value'], currentStats['top1']['value'])
    elif stat == 'duokd' or stat == 'duokills' or stat == 'duowins':
        lifeStats = dataDict['stats']['p10']
        currentStats = dataDict['stats']['curr_p10']
        if stat == 'duokd':
            statString = "@%s %s's Duo K/D: %s (Current Season: %s)" %(user, touser, lifeStats['kd']['value'], currentStats['kd']['value'])
        elif stat == 'duokills':
            statString = "@%s %s's Duo Kills: %s (Current Season: %s)" %(user, touser, lifeStats['kills']['value'], currentStats['kills']['value'])
        elif stat == 'duowins':
            statString = "@%s %s's Duo Wins: %s (Current Season: %s)" %(user, touser, lifeStats['top1']['value'], currentStats['top1']['value'])
    elif stat == 'squadkd' or stat == 'squadkills' or stat == 'squadwins':
        lifeStats = dataDict['stats']['p9']
        currentStats = dataDict['stats']['curr_p9']
        if stat == 'squadkd':
            statString = "@%s %s's Squad K/D: %s (Current Season: %s)" %(user, touser, lifeStats['kd']['value'], currentStats['kd']['value'])
        elif stat == 'squadkills':
            statString = "@%s %s's Squad Kills: %s (Current Season: %s)" %(user, touser, lifeStats['kills']['value'], currentStats['kills']['value'])
        elif stat == 'squadwins':
            statString = "@%s %s's Squad Wins: %s (Current Season: %s)" %(user, touser, lifeStats['top1']['value'], currentStats['top1']['value'])
    elif stat == 'kd' or stat == 'kills' or stat == 'wins':
        lifeStats = dataDict['lifeTimeStats']
        if stat == 'kd':
            data = lifeStats[11]
            statString = "@%s %s's Lifetime K/D: %s" %(user, touser, data['value'])
        elif stat == 'kills':
            data = lifeStats[10]
            statString = "@%s %s has %s Lifetime Kills" %(user, touser, data['value'])
        elif stat == 'wins':
            data = lifeStats[8]
            statString = "@%s %s has %s Lifetime Wins" %(user, touser, data['value'])
    else:
        statString = "Invalid statistic requested. Supported statistics are: solokd, solokills, solowins, duokd, duokills, duokd, squadkd, squadwins, squadkills, kd, kills, wins. Command format is !fortnite user statistic platform"
    return statString