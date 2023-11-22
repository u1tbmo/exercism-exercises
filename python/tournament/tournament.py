def tally(rows: list[str]):
    table = ["Team                           | MP |  W |  D |  L |  P"]
    team_stats: dict[str, list[int]] = {}

    for line in rows:
        t1, t2, outcome = line.split(";")
        if t1 not in team_stats:
            team_stats[t1] = [0, 0, 0, 0, 0]
        if t2 not in team_stats:
            team_stats[t2] = [0, 0, 0, 0, 0]

        team_stats[t1][0] += 1
        team_stats[t2][0] += 1

        if outcome == "win":
            team_stats[t1][1] += 1
            team_stats[t1][4] += 3
            team_stats[t2][3] += 1
        elif outcome == "loss":
            team_stats[t2][1] += 1
            team_stats[t2][4] += 3
            team_stats[t1][3] += 1
        elif outcome == "draw":
            team_stats[t1][2] += 1
            team_stats[t2][2] += 1
            team_stats[t1][4] += 1
            team_stats[t2][4] += 1

    team_stats = dict(sorted(team_stats.items(), key=lambda x: (-x[1][4], x[0])))
    for team, details in team_stats.items():
        table.append(
            f"{team:<31}| {details[0]:2} | {details[1]:2} | {details[2]:2} | {details[3]:2} | {details[4]:2}"
        )
    return table
