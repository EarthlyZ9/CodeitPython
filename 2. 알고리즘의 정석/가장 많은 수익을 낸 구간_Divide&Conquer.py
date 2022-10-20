# divide한 것을 합쳐주는 함수
def max_crossing_sum(profits, start, end):
    mid_index = (start + end) // 2
    sum1 = 0
    sum_list1 = []
    sum2 = 0
    sum_list2 = []
    for i in range(mid_index, start - 1, -1):
        sum1 = sum1 + profits[i]
        sum_list1.append(sum1)

    for j in range(mid_index + 1, end + 1):
        sum2 = sum2 + profits[j]
        sum_list2.append(sum2)

    return max(sum_list1) + max(sum_list2)


# 재귀함수로 구현한 최종 함수(나눠주는 함수)
def sublist_max(profits, start, end):

    if start == end:
        return profits[start]
    mid_index = (start + end) // 2
    return max(
        sublist_max(profits, start, mid_index),
        sublist_max(profits, mid_index + 1, end),
        max_crossing_sum(profits, start, end),
    )


list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max(list2, 0, len(list2) - 1))

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max(list3, 0, len(list3) - 1))

list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
print(sublist_max(list4, 0, len(list4) - 1))
