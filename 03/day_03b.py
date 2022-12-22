with open('input.txt') as f:
    rucksack_list = f.read().split('\n')
    score = 0
    for i in range(0, rucksack_list.__len__(), 3):
        elf_group = rucksack_list[i:i+3]
        item_set_1 = set(elf_group[0])
        item_set_2 = set(elf_group[1])
        item_set_3 = set(elf_group[2])
        badge = item_set_1.intersection(item_set_2, item_set_3)
        if next(iter(badge)).islower(): diff = 96
        else: diff = 64 - 26
        score += (ord(next(iter(badge))) - diff)
    print(score)