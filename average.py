import json
import math
import requests

myRoster = requests.get('https://on-paper-sports.s3.us-east-2.amazonaws.com/basketball/NBA2019-20v4.json', timeout=5).text
JSONRoster = json.loads(myRoster)
print('loaded roster')

f = open("roster2.json", "r")
roster = f.read()
JSONRoster2 = json.loads(roster)



def getAvg():
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

    for player in JSONRoster2['freeAgents']['roster']:
        ros2Size +=1
        t2Off += player['off']
        t2Def += player['def']
        t2Three += player['threePoint']
        t2Ft += player['ft']
        t2Reb += player['reb']

    print(f'avgOff: {(tOff/rosSize) - (t2Off/ros2Size)}')
    print(f'avgDef: {(tDef/rosSize)- (t2Def/ros2Size)}')
    print(f'avgThree: {(tThree/rosSize) - (t2Three/ros2Size)}')
    print(f'avgReb: {(tReb/rosSize) - (t2Reb/ros2Size)}')

    updateRoster('off', (tOff/rosSize) - (t2Off/ros2Size))
    updateRoster('def', (tDef/rosSize)- (t2Def/ros2Size))
    updateRoster('reb', (tReb/rosSize) - (t2Reb/ros2Size))
    save()


def updateRoster(attribute, growth):
    print(len(JSONRoster2['teams']))
    for team in JSONRoster2['teams']:
        print team['name']
        for player in team['roster']:
            if team['name'] == 'Portland Trail Blazers':
                print(player['name'])
                print(growth)
            player[attribute] += round(growth)
            if(player[attribute] > 99):
                player[attribute] = 99

    for player in JSONRoster2['freeAgents']['roster']:
        for player in team['roster']:
            player[attribute] += round(growth)
            if(player[attribute] > 99):
                player[attribute] = 99


def save():
    f = open("roster3.json", "w")
    f.write(json.dumps(JSONRoster2))
    f.close()
        

getAvg()