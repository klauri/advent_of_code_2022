
with open('day_01_data.txt') as f:
    cal_data = f.read().rstrip('\n').split('\n\n')
    added_cals = []
    for elf in cal_data:
        cal_count = 0
        for elf in elf.split('\n'):
            cal_count += int(elf)
            added_cals.append(cal_count)
added_cals.sort(reverse=True)
print(sum(added_cals[:3]))