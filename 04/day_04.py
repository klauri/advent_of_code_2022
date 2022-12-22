with open('input.txt') as f:
    subset_counter = 0
    overlap_counter = 0
    pairs_list = f.read().split('\n')
    for pair in pairs_list:
        first = pair.split(',')[0].split('-')
        second = pair.split(',')[1].split('-')

        first_range = range(int(first[0]), int(first[1]) + 1)
        second_range = range(int(second[0]), int(second[1]) + 1)
        
        sec_1 = set(first_range)
        sec_2 = set(second_range)
        if sec_1 <= sec_2 or sec_2 <= sec_1:
            subset_counter += 1
        if len(sec_1.intersection(sec_2)) != 0:
            overlap_counter += 1
    print(subset_counter, overlap_counter)
        