import json

f = open("roster.json", "r")
roster = f.read()
JSONRoster = json.loads(roster)

def main():
    for team in JSONRoster['teams']:
        for player in team['roster']:
            removeDuplicates(player)
            team['roster'].append(player)

    for player in JSONRoster['freeAgents']['roster']:
        removeDuplicates(player)
        JSONRoster['freeAgents']['roster'].append(player)


    f = open("roster2.json", "w")
    f.write(json.dumps(JSONRoster))
    f.close()



def removeDuplicates(player):
    duplicatesRemoved = 0
    for team in JSONRoster['teams']:
        for comparisonPlayer in team['roster'][:]:
            if player['name'] == comparisonPlayer['name']:
                duplicatesRemoved += 1
                team['roster'].remove(comparisonPlayer)

    comparisonPlayer = None
    for comparisonPlayer in JSONRoster['freeAgents']['roster'][:]:
            if player['name'] == comparisonPlayer['name']:
                print(player['name'])
                duplicatesRemoved += 1
                JSONRoster['freeAgents']['roster'].remove(comparisonPlayer)

    if duplicatesRemoved > 0:
        print(f"{duplicatesRemoved} copies were removed of {player['name']}")





def isEqual(p1, p2):
    if(p1['name'] in p2['name']):
        return True
    
    return False


def delete(players):
    for player in players:
        if(player in JSONRoster['freeAgents']['roster']):
            JSONRoster['freeAgents']['roster'].pop(JSONRoster['freeAgents']['roster'].index(player))





if __name__ == '__main__':
    main()
