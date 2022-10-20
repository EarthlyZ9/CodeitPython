def max_product(left_cards, right_cards):
    all_case = []
    for i in left_cards:
        for j in right_cards:
            single_case = i * j
            all_case.append(single_case)
    return max(all_case)


print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))
