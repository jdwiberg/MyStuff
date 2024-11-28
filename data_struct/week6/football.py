

def main():
    game = []
    for i in range(2):
        team = input(f"Enter team {i+1}'s scores\nFormat: Td Fg Sft Pa 2pc\n").split()
        if len(team) != 5:
            print("Input error, please try again.")
            break
        for i in range(len(team)):
            try:
                team[i] = int(team[i])
            except:
                print("Input integers only")
                break
            if team[i] < 0:
                break
        score = 0
        score += team[0] * 6
        score += team[1] * 3
        score += (team[2] + team[4]) * 2
        score += team[3] * 1

        game.append(score)

    print(f"Team 1 scored {game[0]} points.")
    print(f"Team 2 scored {game[1]} points.")
    if game[0] > game[1]:
        print("Team 1 is the winner")
    elif game[1] > game[0]:
        print("Team 2 is the winner")
    else:
        print("The game was a tie!")


main()
