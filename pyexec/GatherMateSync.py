#!/usr/bin/env python3

from wlog import parseLuaObjectsFromFile
from wlog import saveAsLuaString

from httplib2 import HTTPConnectionWithTimeout
from urllib.parse import urlencode
from ast import literal_eval


def request(method, data=b''):
    assert(method == 'GET' or method == 'POST')

    if isinstance(data, str):
        data = data.encode(encoding='utf-8')

    con = HTTPConnectionWithTimeout('wow.fry-soft.at')
    con.request(method=method, url='/GatherMateSync.php', body=data)

    resp = con.getresponse()
    if resp.status != 200:
      print('Requesting data from server failed with:', resp.status, resp.reason)
      exit(0)

    status = resp.readline()[:-1]
    returnData = resp.readline()[:-1]
    if status == b'SUCCESS':
        if returnData == b'':
            return None
        return returnData.decode(encoding='utf-8')
    elif status == b'ERROR':
        print('Server responded with an error:')
        print(returnData.decode(encoding='utf-8'))
        exit(1)
    else:
        print('Invalid return status:', status)
        print(returnData)
        exit(1)


def getData() -> dict:
    returnData = request(method='GET')
    return literal_eval(returnData)


def putData(data: dict):
    request(method='POST', data=str(data))


# def loadData() -> dict:
#     dbKeys = ['GatherMate2HerbDB', 'GatherMate2MineDB', 'GatherMate2FishDB', 'GatherMate2TreasureDB']
#     lua = parseLuaObjectsFromFile('GM2.lua')
#     data = dict()
#     for key in dbKeys:
#         if key not in lua:
#             print(key, 'missing from LuaFile!')
#             exit(1)
#         data[key] = lua[key]
#     return data


# def saveData(newData):
#     oldData = parseLuaObjectsFromFile('GM2.lua')
#     dbKeys = ['GatherMate2HerbDB', 'GatherMate2MineDB', 'GatherMate2FishDB', 'GatherMate2TreasureDB']
#     for key in dbKeys:
#         if key not in oldData:
#             print(key, 'missing from oldData!')
#             exit(1)
#         if key not in newData:
#             print(key, 'missing from newData!')
#             exit(1)
#         oldData[key] = newData[key]
    
#     toLuaObject(oldData, 'GM2_rec.lua')


def updateData(fname: str):
    dbKeys = ['GatherMate2HerbDB', 'GatherMate2MineDB', 'GatherMate2FishDB', 'GatherMate2TreasureDB']

    data = parseLuaObjectsFromFile(fname)
    serverData = getData()

    for name in dbKeys:
        if name not in data:
            print(name, 'missing from local data!')
            exit(1)
        if name not in serverData:
            print(name, 'missing from server data!')
            exit(1)

        for zone in serverData[name]:
            if zone not in data[name]:
                data[name][zone] = serverData[name][zone]
            else:
                for coord in serverData[name][zone]:
                    data[name][zone][coord] = serverData[name][zone][coord]
               
    saveAsLuaString(data=data, fname=fname)

    for name in dbKeys:
        serverData[name] = data[name]
    putData(serverData)


updateData('/mnt/c//Program Files (x86)/World of Warcraft/_classic_/WTF/Account/133617675#2/SavedVariables/GatherMate2.lua')
