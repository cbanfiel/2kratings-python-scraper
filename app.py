from bs4 import BeautifulSoup
import requests
import re 
import json
import time

myRoster = requests.get('https://on-paper-sports.s3.us-east-2.amazonaws.com/basketball/NBA2019-20v4.json', timeout=5).text
JSONRoster = json.loads(myRoster)
print('loaded roster')


def main():
    parse()
    f = open("roster.json", "w")
    f.write(json.dumps(JSONRoster))
    f.close()


def parse():
    movedPlayers = []
    for team in JSONRoster["teams"]:
        print(team['name'])
        for player in team["roster"]:
            teamName = ''
            name = player["name"]
            name = name.replace(" ", "-")
            name = name.replace(".", "")
            src = requests.get(f'https://www.2kratings.com/{name}').text
            soup = BeautifulSoup(src, 'html.parser')
            info = {}
            ps = soup.findAll('p', class_='text-muted mb-0')
            for p in ps:
                if('Team:' in p.text):
                    if(not 'Nationality:' in p.text):
                        teamName = p.text.replace("Team: ", "")
                if('Jersey:' in p.text):
                    if(not 'Nationality:' in p.text):
                        number = p.text.replace("Jersey: #", "")
                        player['number'] = int(number)

            h5s = soup.findAll('h5', class_='mb-0')
            for h5 in h5s:
                temp = re.compile("([0-9]+)([a-zA-Z ]+)") 
                try:
                    res = temp.match(h5.text).groups() 
                    info.update({res[1]: int(res[0])})
                except:
                    pass
            lis = soup.findAll('li', class_='mb-1')
            for li in lis:
                temp = re.compile("([0-9]+)([a-zA-Z ]+)") 
                try:
                    res = temp.match(li.text).groups() 
                    info.update({res[1]: int(res[0])})
                    
                except:
                    break
            ratings = convert(info, player)
            player.update(ratings)
            if(len(teamName) > 3):
                if(team['name'] != teamName):
                    print(f'moved {player["name"]} to the {teamName}')
                    movedPlayers.append({'player': player, 'team': teamName})
            time.sleep(.5)

    team = JSONRoster['freeAgents']
    print(team['name'])
    for player in team["roster"]:
        name = player["name"]
        name = name.replace(" ", "-")
        src = requests.get(f'https://www.2kratings.com/{name}').text
        soup = BeautifulSoup(src, 'html.parser')
        info = {}
        ps = soup.findAll('p', class_='text-muted mb-0')
        for p in ps:
            if('Team:' in p.text):
                if(not 'Nationality:' in p.text):
                    teamName = p.text.replace("Team: ", "")
            if('Jersey:' in p.text):
                if(not 'Nationality:' in p.text):
                    number = p.text.replace("Jersey: #", "")
                    player['number'] = int(number)

        h5s = soup.findAll('h5', class_='mb-0')
        for h5 in h5s:
            temp = re.compile("([0-9]+)([a-zA-Z ]+)") 
            try:
                res = temp.match(h5.text).groups() 
                info.update({res[1]: int(res[0])})
            except:
                pass
        lis = soup.findAll('li', class_='mb-1')
        for li in lis:
            temp = re.compile("([0-9]+)([a-zA-Z ]+)") 
            try:
                res = temp.match(li.text).groups() 
                info.update({res[1]: int(res[0])})
                
            except:
                break
        ratings = convert(info, player)
        player.update(ratings)
        if(len(teamName) > 3):
            if(team['name'] != teamName):
                print(f'moved {player["name"]} to the {teamName}')
                movedPlayers.append({'player': player, 'team': teamName})
        time.sleep(.5)
    movePlayers(movedPlayers)

def convert(ratings, player):
    #off def three reb ft
    #off = closeshot + midrange + three + shotiq + layup + standingdunk + dirivingdun + hook + fade
    try:
        offense = int(ratings[' Outside Scoring']) if int(ratings[' Outside Scoring']) > int(ratings[' Inside Scoring']) else int(ratings[' Inside Scoring'])
        defense = ratings[' Defending'] 
        threePoint = ratings['Three']
        rebound = ratings[' Rebounding']
        freeThrow = ratings['Free Throw']
        return{"off": int(offense), "def": int(defense), "threePoint": int(threePoint), "reb": int(rebound), "ft": int(freeThrow)}
    except Exception as e:
        print('Error: ' +  player['name'] + str(e))
        return {}

def movePlayers(movedPlayers):
    freeAgents = []
    for trade in movedPlayers:
        movedSuccessfully = False
        for team in JSONRoster['teams']:
            if(trade['player'] in team['roster']):
                team['roster'].remove(trade['player'])

            if(team['name'] == trade['team']):
                team['roster'].append(trade['player'])
                movedSuccessfully = True
        if(not movedSuccessfully):
            freeAgents.append(trade['player'])
        
    print(len(freeAgents))
    JSONRoster['freeAgents']['roster'] = JSONRoster['freeAgents']['roster'] + freeAgents



if __name__ == "__main__":
    main()