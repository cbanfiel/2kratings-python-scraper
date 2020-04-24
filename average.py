from bs4 import BeautifulSoup
import requests
import re
import json
import time

myRoster = requests.get('https://on-paper-sports.s3.us-east-2.amazonaws.com/basketball/NBA2019-20v4.json', timeout=5).text
JSONRoster = json.loads(myRoster)
print('loaded roster')

f = open("NBA2019-20v5.json", "r")
roster = f.read()
JSONRoster2 = json.loads(roster)

tOff= 0
tDef = 0
tThree = 0
tFt = 0
tReb = 0
rosSize = 0

t2Off= 0
t2Def = 0
t2Three = 0
t2Ft = 0
t2Reb = 0
ros2Size = 0

def getAvg():
    for team in JSONRoster['teams']:
        for player in team['roster']:
            rosSize +=1
            tOff += player['off']
            tDef += player['def']
            tThree += player['threePoint']
            tFt += player['ft']
            tReb += player['reb']

    for player in JSONRoster['freeAgents']['roster']:
        rosSize +=1
        tOff += player['off']
        tDef += player['def']
        tThree += player['threePoint']
        tFt += player['ft']
        tReb += player['reb']

    for team in JSONRoster2['teams']:
        for player in team['roster']:
            ros2Size +=1
            t2Off += player['off']
            t2Def += player['def']
            t2Three += player['threePoint']
            t2Ft += player['ft']
            t2Reb += player['reb']

    for player in JSONRoster['freeAgents']['roster']:
        ros2Size +=1
        t2Off += player['off']
        t2Def += player['def']
        t2Three += player['threePoint']
        t2Ft += player['ft']
        t2Reb += player['reb']

    print(f'avgOff: {tOff/rosSize}')
    print(f'avgDef: {tDef/rosSize}')
    print(f'avgThree: {tThree/rosSize}')
    print(f'avgFt: {tFt/rosSize}')
    print(f'avgReb: {tReb/rosSize}')


def updateRoster(attribute, growth):
        for team in JSONRoster['teams']:
            for player in team['roster']:
                player[attribute] += floor(growth)

        for player in JSONRoster['freeAgents']['roster']:
            for player in team['roster']:
                player[attribute] += floor(growth)
