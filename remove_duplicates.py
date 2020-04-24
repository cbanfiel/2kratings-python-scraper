import json

f = open("roster.json", "r")
roster = f.read()
JSONRoster = json.loads(roster)


def main():
    deletePlayers = []
    for player in JSONRoster['freeAgents']['roster']:
        for ply in JSONRoster['freeAgents']['roster']:
            if(player['name'] in ply['name'] and not player['name'] in deletePlayers):
                deletePlayers.append(ply)

    delete(deletePlayers)
    f = open("roster2.json", "w")
    f.write(json.dumps(JSONRoster))
    f.close()




def delete(players):
    for player in players:
        for team in JSONRoster['teams']:
            if(player in team['roster']):
                team['roster'].remove(player)





if __name__ == '__main__':
    main()
