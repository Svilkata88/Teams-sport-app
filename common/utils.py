from teams.models import Team


def postmatch_stats_update(match, team1_players=None, team2_players=None):
    # when update player.models with player stats will be applied logic for their update
    # if not team1_players:
    #     team1_players = match.home_team.players.all()
    # if not team2_players:
    #     team2_players = match.away_team.players.all()

    team1_win = (match.home_team_score > match.away_team_score)
    team2_win = (match.home_team_score < match.away_team_score)
    draw = (match.home_team_score == match.away_team_score)

    if team1_win:
        match.home_team.wins += 1
        match.away_team.loses += 1
    elif team2_win:
        match.away_team.wins += 1
        match.home_team.loses += 1
    elif draw:
        match.home_team.draws += 1
        match.away_team.draws += 1

    match.home_team.save()
    match.away_team.save()
        # after func execution instances should be saved in db outside the func


def update_ranking():
    # може евентуално да се подобри
    teams = Team.objects.all()

    all_team_points = {}  # { team name: total_points }

    for team in teams:
        win_points = team.wins * 3
        draw_points = team.draws * 1
        total_points = win_points + draw_points

        all_team_points[team.name] = total_points

    all_team_points_sorted = dict(sorted(all_team_points.items(), key=lambda item: item[1], reverse=True))

    for index, team in enumerate(all_team_points_sorted):
        all_team_points_sorted[team] = index + 1

    for team in teams:
        team.rank = all_team_points_sorted[team.name]


# def run_updates(match: Matches):
#     postmatch_stats_update(match)
#     update_ranking()
#     match.save()
#     match.home_team.save()
#     match.away_team.save()
