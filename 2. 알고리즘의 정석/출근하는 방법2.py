def staircase(stairs, possible_steps):
    stairs_table = [1, 1]
    for i in range(2, stairs + 1):
        split_sum = 0
        for step in possible_steps:
            if i - step < 0:
                split_sum = split_sum
            else:
                split_sum = split_sum + stairs_table[i - step]
        stairs_table.append(split_sum)
    return stairs_table[stairs]


print(staircase(4, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))
