import tui

def list_years(data):
    years = set()
    tui.started("Listing years...")
    for records in data:
        years.add(records[9])
    tui.display_years(years)
    tui.completed()

def tally_medals(data):
    tui.started("Tallying medals...")
    medals = {"Gold": 0, "Silver": 0, "Bronze": 0}


    for records in data:
        if records[14] == "Gold":
            medals['Gold'] += 1
        elif records[14] == "Silver":
            medals['Silver'] += 1
        elif records[14] == "Bronze":
            medals['Bronze'] += 1

    tui.display_medal_tally(medals)
    tui.completed()

def tally_team_medals(data):
    tui.started("Tallying medals for each team...")
    teams = {}
    for records in data:
        team = records[6]
        medal = records[14]
        if medal not in ('Gold','Silver','Bronze'):
            continue
        if team in teams:
            teams[team][medal] += 1
        else:
            teams[team] = {"Gold": 0, "Silver": 0, "Bronze": 0}
            teams[team][medal] += 1

    tui.display_team_medal_tally(teams)
    tui.completed()
