
with open('input.txt', 'r') as f:
    lines = f.readlines()

scores = []
game_score = []
for line in lines:
    game_score = [line.split(' ')[0], line.split(' ')[1][0]]
    scores.append(game_score)
# rock: 1
# paper: 2
# scissors: 3
# lose: 0
# draw: 3
# win: 6
# X = lose
# Y = draw
# Z = win

score_calc = []
for score in scores:
    score_calc_game = 0
    if score[1] == 'X':
        score_calc_game = 0
        if score[0] == 'A':
            score_calc_game += 3
        elif score [0] == 'B':
            score_calc_game += 1
        else:
            score_calc_game += 2
    elif score[1] == 'Y':
        score_calc_game = 3
        if score[0] == 'A':
            score_calc_game += 1
        elif score [0] == 'B':
            score_calc_game += 2
        else:
            score_calc_game += 3
    elif score[1] == 'Z':
        score_calc_game = 6
        if score[0] == 'A':
            score_calc_game += 2
        elif score [0] == 'B':
            score_calc_game += 3
        else:
            score_calc_game += 1
    score_calc.append(score_calc_game)
print(score_calc)
print(sum(score_calc))