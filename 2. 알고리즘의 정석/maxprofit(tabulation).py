def max_profit(price_list, count):
    max_table = [price_list[0], price_list[1]]
    possible_cases = []
    for i in range(2, count + 1):
        if i < len(price_list):
            profit = price_list[i]
        else:
            profit = 0

        possible_cases.append(profit)

        for j in range(1, i // 2 + 1):
            possible_cases.append(max_table[i - j] + max_table[j])

        max_table.append(max(possible_cases))

    return max_table[count]


# 테스트
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
