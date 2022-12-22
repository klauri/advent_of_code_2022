choice_score = 0
round_score = 0
with open('input.txt') as f:
    for round in f.read().split('\n'):
        if round[2:3] == 'X':
            choice_score += 1
        elif round[2:3] == 'Y':
            choice_score += 2
        else:
            choice_score += 3
        if round[0:1] == 'A':
            if round[2:3] == 'X':
                round_score += 3
            if round[2:3] == 'Y':
                round_score += 6
            if round[2:3] == 'Z':
                round_score += 0
        if round[0:1] == 'B':
            if round[2:3] == 'X':
                round_score += 0
            if round[2:3] == 'Y':
                round_score += 3
            if round[2:3] == 'Z':
                round_score += 6
        if round[0:1] == 'C':
            if round[2:3] == 'X':
                round_score += 6
            if round[2:3] == 'Y':
                round_score += 0
            if round[2:3] == 'Z':
                round_score += 3
    print(choice_score + round_score)
