import json

f = open("roster.json", "r")
roster = f.read()
JSONRoster = json.loads(roster)


def main():
    deletePlayers = []
    deletedNames = []
    for player in JSONRoster['freeAgents']['roster']:
        for ply in JSONRoster['freeAgents']['roster']:
            if(player['name'] is ply['name'] and ply['name'] not in deletedNames):
                print(ply['name'])
                deletePlayers.append(ply)
                deletedNames.append(ply['name'])


    delete(deletePlayers)
    f = open("roster2.json", "w")
    f.write(json.dumps(JSONRoster))
    f.close()




def delete(players):
    for player in players:
        if(player in JSONRoster['freeAgents']['roster']):
            JSONRoster['freeAgents']['roster'].pop(JSONRoster['freeAgents']['roster'].index(player))





if __name__ == '__main__':
    main()
