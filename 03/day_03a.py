with open('input.txt') as f:
    score = 0
    rucksack_list = f.read().split('\n')
    for rucksack in rucksack_list:
        l = rucksack.__len__()
        comp1 = rucksack[0:(l//2)]
        comp2 = rucksack[(l//2):l]
        comp_set = set((comp1, comp2))
        for char1 in comp1:
            if char1 in comp2:
                if char1.islower(): diff = 96
                else: diff = 64 - 26
                score += (ord(char1) - diff)
                break
    print(score)