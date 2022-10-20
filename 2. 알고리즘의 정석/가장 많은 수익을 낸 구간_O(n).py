def sublist_max(profits):
    j = 0
    while j < len(profits):
        if profits[j] > 0:
            start = j
            break
        j += 1

    sum = 0
    sum_list = []
    max_amount = 0
    for i in range(j, len(profits)):
        sum += profits[i]
        sum_list.append(sum)
        max_amount = max(sum_list)
    return max_amount


# # 부분문제 1: 리스트의 마지막 요소를 제외한 최대 수익 구간
# # 부분문제 2: 리스트의 마지막 요소를 포함한 모든 구간 중 최대 수익 구간
# def sublist_max(profits):
#     max_profit_so_far = profits[0]
#     # 해당 시점에서의 가장 끝 요소를 포함하는 구간의 최대 합
#     max_check = profits[0]
#     for i in range(1, len(profits)):
#         max_check = max(max_check)


# 테스트
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))
