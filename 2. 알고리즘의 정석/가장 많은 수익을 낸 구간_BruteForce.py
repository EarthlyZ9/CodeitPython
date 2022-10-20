def sublist_max(profits):
    sum_lists = []
    for i in range(0, len(profits)):
        sum = 0
        for j in range(i, len(profits)):
            sum = sum + profits[j]
            sum_lists.append(sum)
    return max(sum_lists)


# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))
