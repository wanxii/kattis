import sys

favorite_team = 1

class Team:

    def __init__(self, num_solved, total_panelty):
        self.num_solved = num_solved
        self.total_panelty = total_panelty


def score_better(team, favorite_team):
    if team.num_solved > favorite_team.num_solved:
        return True
    if team.num_solved == favorite_team.num_solved:
        if team.total_panelty < favorite_team.total_panelty:
            return True
    return False


def remove_worse_teams(prior_teams, team):
    if len(prior_teams) > 0:
        sorted_lst = {k: v for k, v in sorted(prior_teams.items(),
                    key=lambda x: (x[1].num_solved, -x[1].total_panelty))}
        for k, t in sorted_lst.items():
            if not score_better(t, team):
                prior_teams.pop(k)
                continue
            return


def update_score(team_dictionary, team, panelty):
    if team not in team_dictionary:
        team_dictionary[team] = Team(0, 0)
    team_dictionary[team].num_solved += 1
    team_dictionary[team].total_panelty += panelty


def compute_rank_records(input, team):
    n, m = map(int, input.readline().split())
    team_dic = {team: Team(0, 0)}
    prior_teams = {}
    rv = []

    for _ in range(m):
        t, p = map(lambda x: int(x.rstrip()), input.readline().split())
        assert 1 <= t <= n
        update_score(team_dic, t, p)
    
        if t == team:
            remove_worse_teams(prior_teams, team_dic[t])
        else:
            if t not in prior_teams:
                if score_better(team_dic[t], team_dic[team]):
                    prior_teams[t] = team_dic[t]
        rv.append(len(prior_teams) + 1)

    return rv


def main(input):
    for record in compute_rank_records(input, favorite_team):
        print(record)


if __name__ == '__main__':
    main(sys.stdin)