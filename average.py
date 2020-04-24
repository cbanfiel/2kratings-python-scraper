import json
import math
import requests

# myRoster = requests.get('https://on-paper-sports.s3.us-east-2.amazonaws.com/basketball/NBA2019-20v4.json', timeout=5).text
# JSONRoster = json.loads(myRoster)
# print('loaded roster')

f = open("roster2.json", "r")
roster = f.read()
JSONRoster2 = json.loads(roster)

def main():
    updateRoster()
    save()

def scaleBetween(unscaledNum, minAllowed, maxAllowed, min, max):
    return (
        ((maxAllowed - minAllowed) * (unscaledNum - min)) / (max - min) + minAllowed
    )



def updateRoster():
    print(len(JSONRoster2['teams']))
    for team in JSONRoster2['teams']:
        print(team['name'])
        for player in team['roster']:
            player['def'] = round(scaleBetween(player['def'],50,99,30,94))
            player['off'] = round(scaleBetween(player['off'],50,99,42,96))
            player['reb'] = round(scaleBetween(player['reb'],50,99,30,94))

            if (player['off'] > 99):
                player['off'] = 99
                
            if (player['def'] > 99):
                player['def'] = 99

def save():
    f = open("roster3.json", "w")
    f.write(json.dumps(JSONRoster2))
    f.close()
        

main()