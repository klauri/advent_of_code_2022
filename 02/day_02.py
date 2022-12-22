choice_score = 0
round_score = 0
with open('input.txt') as f:
    for round in f.read().split('\n'):
        if round[2:3] == 'X':
            round_score += 0
            if round[0:1] == 'A':
                choice_score += 3
            elif round[0:1] == 'B':
                choice_score += 1
            else:
                choice_score += 2
        elif round[2:3] == 'Y':
            round_score += 3
            if round[0:1] == 'A':
                choice_score += 1
            elif round[0:1] == 'B':
                choice_score += 2
            else:
                choice_score += 3
        else:
            round_score += 6
            if round[0:1] == 'A':
                choice_score += 2
            elif round[0:1] == 'B':
                choice_score += 3
            else:
                choice_score += 1
    print(choice_score + round_score)
