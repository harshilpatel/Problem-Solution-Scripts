# harshil912@gmail.com

test_cases = int(raw_input())


test_case_list = []
for i in range(test_cases):
    test_case_list.append( [int(i) for i in raw_input().split(' ')] )

for i in test_case_list:
    team_options = sorted(i)
    team_options.reverse()
    teams = []
    temp_team = []
    temp_team.append(team_options[0])
    
    for item in range(1, len(team_options)):
        if team_options[item] + 1 != team_options[item - 1]:
            teams.append(temp_team)
            temp_team = []
        else:
            temp_team.append(team_options[item])
    if len(team_options) > 0:
        teams.append(team_options)

    if [] in teams:
        teams.remove([])
    for i in teams:
        i = list(set(i))
    print teams