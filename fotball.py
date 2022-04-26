from typing import OrderedDict


Iran = OrderedDict = {
    'name' : 'Iran',
    "wins":0,
    "loses": 0, 
    "draws": 0,
    'goal difference': 0, 
    'points' : 0
    }
Spain = OrderedDict  = {
    'name' : 'Spain',
    "wins":0,
    "loses": 0, 
    "draws": 0,
    'goal difference': 0, 
    'points' : 0
    }
Portugal = OrderedDict  = {
    'name' : 'Portugal',
    "wins":0,
    "loses": 0, 
    "draws": 0,
    'goal difference': 0, 
    'points' : 0
    }
Morocco = OrderedDict  = {
    'name' : 'Morocco',
    "wins":0,
    "loses": 0, 
    "draws": 0,
    'goal difference': 0, 
    'points' : 0
}   

def handle_result(team1, team2) :

    result = input().split('-')
    
    team1['goal difference'] = team1['goal difference'] + int(result[0]) - int(result[1])
    team2['goal difference'] = team2['goal difference'] + int(result[1]) - int(result[0])


    if result[0] > result[1] :
        team1 ['wins'] = team1 ['wins'] + 1
        team2 ['loses'] = team2 ['loses'] + 1
        team1 ['points'] = team1 ['points'] + 3
    elif result[0] < result[1]:
        team2 ['wins'] = team2 ['wins'] + 1
        team1 ['loses'] = team1 ['loses'] + 1
        team2 ['points'] = team2 ['points'] + 3
    else :
        team2 ['draws'] = team2 ['draws'] + 1
        team1 ['draws'] = team1 ['draws'] + 1
        team1 ['points'] = team1 ['points'] + 1
        team2 ['points'] = team2 ['points'] + 1


handle_result(Iran, Spain)
handle_result(Iran, Portugal)
handle_result(Iran, Morocco)
handle_result(Spain, Portugal)
handle_result(Spain, Morocco)
handle_result(Portugal, Morocco)

list = [
    Iran,
    Spain,
    Portugal,
    Morocco
]

list.sort(key = lambda x :  x['name']   )
list.sort(key = lambda x : x['points'], reverse=True  )

def handle_print(team) :
    print(f'{team["name"]}  wins:{team["wins"]} , loses:{team["loses"]} ,  draws:{team["draws"]} ,  goal difference:{team["goal difference"]} ,  points:{team["points"]}')

for i in list:
    handle_print(i)